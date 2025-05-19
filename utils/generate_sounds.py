import os
import argparse
import numpy as np
import networkx as nx
import math

from scipy.io.wavfile import write
from fractions import Fraction


NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def midi_to_freq(midi_note):
    return 440.0 * 2 ** ((midi_note - 69) / 12)

def midi_to_name(midi):
    return f"{NOTE_NAMES[midi % 12]}{midi // 12}"

def generate_envelope(n_samples, samplerate, attack=0.02, decay=0.05, sustain_level=0.7, release=0.1):
    """
    Generate an ADSR envelope for shaping the volume curve.

    Returns:
        ndarray: Envelope array to multiply with waveform.
    """
    a = int(attack * samplerate)
    d = int(decay * samplerate)
    r = int(release * samplerate)
    s = n_samples - (a + d + r)

    if s < 0:  # tone is too short
        s = 0
        d = max(0, n_samples - a - r)

    env = np.concatenate([
        np.linspace(0, 1, a, endpoint=False),
        np.linspace(1, sustain_level, d, endpoint=False),
        np.full(s, sustain_level),
        np.linspace(sustain_level, 0, r)
    ])

    env = np.pad(env, (0, max(0, n_samples - len(env))), mode='constant')
    return env[:n_samples]


def generate_wave(freq, duration=1.5, samplerate=44100, amplitude=0.1, harmonics=[1, 2, 3], apply_env=True):
    """
    Generate a wave with optional harmonics and envelope shaping.

    Args:
        freq (float): Base frequency in Hz.
        duration (float): Length of tone in seconds.
        samplerate (int): Sampling rate in Hz.
        amplitude (float): Base amplitude (0 to 1).
        harmonics (list): Which harmonics to include (1 = fundamental, 2 = 1st overtone, etc.)
        apply_env (bool): Whether to apply ADSR envelope.
    """
    t = np.linspace(0., duration, int(samplerate * duration), endpoint=False)
    wave = np.zeros_like(t)

    # Add harmonics
    for h in harmonics:
        partial_amp = amplitude / (h ** 1.2)  # roll-off higher harmonics
        wave += partial_amp * np.sin(2 * np.pi * freq * h * t)

    # Normalize
    wave /= np.max(np.abs(wave))

    # Apply envelope
    if apply_env:
        env = generate_envelope(len(wave), samplerate)
        wave *= env

    return np.int16(wave * 32767)


def midi_to_name(midi):
    return f"{NOTE_NAMES[midi % 12]}{midi // 12}"

# base freq:
# E2 82.41
# E3 164.81
def scale_eigenvalues_to_midi(eigs, base_freq=164.81, base_midi=40, verbose=True):
    
    """
    Maps eigenvalues to MIDI notes using harmonic ratios relative to the smallest non-zero eigenvalue.
    Also prints the selected ratios and resulting notes for transparency.
    """
    eigs = [v for v in eigs if v > 1e-3]  # skip 0s
    if not eigs:
        return []

    λ_min = min(eigs)
    midi_notes = []

    print (f"Base Freq: {base_freq}")

    print("Harmonic Ratio Mapping (Just Intonation Style):")
    for λ in eigs:
        ratio = λ / λ_min
        # print(f"λ: {λ}")
        # print(f"λ_min: {λ_min}")
        # print(f"Calculated Ratio: {ratio}")
        approx = Fraction(ratio).limit_denominator(16)
        freq = base_freq * (approx.numerator / approx.denominator)
        # print(f"Calculated Freq: {freq}")
        midi = int(np.round(69 + 12 * np.log2(freq / 440.0)))
        name = midi_to_name(midi)
        midi_notes.append(midi)

        if verbose:
            print(f"  λ = {λ:.4f} → ratio ≈ {approx.numerator}/{approx.denominator} → {name} (MIDI {midi})")
    
    print("")

    return midi_notes

def generate_graph_sounds(eigs, out_dir, basename="graph", chord=True, verbose=True):
    os.makedirs(out_dir, exist_ok=True)
    nonzero_eigs = [v for v in eigs if v > 1e-3]
    midi_notes = scale_eigenvalues_to_midi(nonzero_eigs)
    freqs = [midi_to_freq(m) for m in midi_notes]
    names = [midi_to_name(m) for m in midi_notes]

    if not freqs:
        print(f"⚠️  No non-zero eigenvalues for {basename} — skipping chord generation.")
        return
    
    if verbose:
        print(f"Printing frequencies {basename}:")
        for ev, freq in zip(nonzero_eigs, freqs):
            print(f"  λ = {ev:.2f} → {freq}")
        print("")

    if verbose:
        print(f"Generating sounds for {basename}:")
        for ev, name in zip(nonzero_eigs, names):
            print(f"  λ = {ev:.2f} → {name}")
        print("")

    # Sequential tones
    for i, f in enumerate(freqs):
        tone = generate_wave(f)

        filename = f"{out_dir}/{basename}_tone{i+1}.wav"
        write(filename, 44100, tone)

        filename = f"{out_dir}/{basename}_tone{i+1}.mp3"
        write(filename, 44100, tone)

    # Chord version
    if chord and len(freqs) > 0:
        waves = [generate_wave(f, amplitude=0.1).astype(np.float32) / 32767 for f in freqs]
        chord_wave = sum(waves) / len(waves)
        chord_wave = np.int16(np.clip(chord_wave * 32767, -32767, 32767))

        write(f"{out_dir}/{basename}_chord.wav", 44100, chord_wave)
        write(f"{out_dir}/{basename}_chord.mp3", 44100, chord_wave)

def main():
    parser = argparse.ArgumentParser(description="Generate tones from Laplacian eigenvalues of graphs.")
    parser.add_argument("--graph", type=str, required=True,
                        help="Which graph to use: path, star, complete, cycle, etc.")
    parser.add_argument("--n", type=int, default=6, help="Number of nodes")
    parser.add_argument("--basename", type=str, default=None, help="Output filename prefix")
    parser.add_argument("--out_dir", type=str, default="./sounds", help="Where to put output files")
    parser.add_argument("--no-chord", action="store_true", help="Don't generate chord file")

    args = parser.parse_args()

    # Create the graph
    graph_funcs = {
        "path": nx.path_graph,
        "star": nx.star_graph,
        "cycle": nx.cycle_graph,
        "complete": nx.complete_graph,
        "hypercube": lambda n: nx.hypercube_graph(int(np.log2(n))),  # Q_d with 2^d nodes
        "cartesian": lambda n: nx.cartesian_product(nx.path_graph(math.ceil(n/2)), nx.path_graph(2)) # Cartesian with (n/2) by 2 nodes (round up)
    }

    if args.graph not in graph_funcs:
        print("Unsupported graph type. Try one of: path, star, cycle, complete, hypercube.")
        return

    G = graph_funcs[args.graph](args.n)
    L = nx.laplacian_matrix(G).toarray()
    eigs = np.round(np.linalg.eigvalsh(L), 4)

    basename = args.basename or f"{args.graph}{args.n}"
    generate_graph_sounds(eigs, out_dir=args.out_dir, basename=basename, chord=not args.no_chord)
    arpeggiobasename = f"{args.graph}{args.n}_arpeggio"
    generate_sequential_then_chord(eigs, out_dir=args.out_dir, basename=arpeggiobasename)

def generate_sequential_then_chord(eigs, out_dir, basename="output", duration=0.12, pause=0.06, chord_duration=2.0):
    """
    Generates a single WAV file that plays each eigenvalue tone sequentially,
    followed by the full chord.

    Args:
        eigs (list or np.array): Laplacian eigenvalues.
        out_path (str): Path to save the output .wav file.
        duration (float): Duration (in seconds) for each tone.
        pause (float): Silence gap (in seconds) between tones.
        chord_duration (float): Duration (in seconds) for the final chord.
    """
    from scipy.io.wavfile import write

    midi_notes = scale_eigenvalues_to_midi(eigs)
    if not midi_notes:
        print("No non-zero eigenvalues. Skipping sound generation.")
        return

    freqs = [midi_to_freq(m) for m in midi_notes]
    rate = 44100

    # Generate tones
    tones = [generate_wave(f, duration=duration, samplerate=rate, amplitude=0.1) for f in freqs]
    silence = np.zeros(int(rate * pause), dtype=np.int16)

    # Combine tones with pauses
    sequence = []
    for tone in tones:
        sequence.append(tone)
        sequence.append(silence)

    # Final chord
    chord = sum([generate_wave(f, duration=chord_duration, samplerate=rate, amplitude=0.1).astype(np.float32) / 32767 for f in freqs])
    max_val = np.max(np.abs(chord))
    if max_val > 0:
        chord = chord / max_val  # normalize to [-1.0, 1.0]
    chord = np.int16(chord * 32767)

    # Concatenate everything
    full_audio = np.concatenate(sequence + [chord])

    max_val = np.max(np.abs(full_audio))
    if max_val > 0:
        full_audio = full_audio / max_val
    full_audio = np.int16(full_audio * 32767 * 0.8)

    write(f"{out_dir}/{basename}.wav", rate, full_audio)
    write(f"{out_dir}/{basename}.mp3", rate, full_audio)
    print(f"✔️ Arpeggio wave file saved to {out_dir}/{basename}.wav and {out_dir}/{basename}.mp3")

if __name__ == "__main__":
    main()
