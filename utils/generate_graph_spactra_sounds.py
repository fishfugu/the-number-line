import numpy as np
from scipy.io.wavfile import write

def generate_tone(eigenvalue, filename, duration=1.5, base_freq=220):
    samplerate = 44100
    t = np.linspace(0., duration, int(samplerate * duration))
    freq = base_freq + 100 * eigenvalue
    amplitude = 0.5 * np.sin(2. * np.pi * freq * t)
    wave = np.int16(amplitude * 32767)
    write(filename, samplerate, wave)

# Example graphs:
import networkx as nx

G1 = nx.path_graph(4)
G2 = nx.star_graph(3)

L1 = nx.laplacian_matrix(G1).toarray()
L2 = nx.laplacian_matrix(G2).toarray()

λ1 = np.linalg.eigvalsh(L1)[1]
λ2 = np.linalg.eigvalsh(L2)[1]

generate_tone(λ1, "./audio/graph1.wav")
generate_tone(λ2, "./audio/graph2.wav")
