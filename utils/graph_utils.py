import numpy as np
from manimlib import *
import networkx as nx

def draw_graph(G, layout, node_radius=0.08, font='Consolas', scale=0.3, label_offset=0.1):
    """
    Converts a NetworkX graph into Manim Dots, Lines, and Text labels.

    Args:
        G (networkx.Graph): The graph to render.
        layout (dict): Dictionary of node positions as 3D numpy arrays.
        node_radius (float): Radius of each node dot.
        font (str): Font to use for labels.
        scale (float): Scale factor for label size.
        label_offset (float): Distance between dot and label.

    Returns:
        tuple: (list of Dots, list of Lines, list of Text labels)
    """
    dots = []
    lines = []
    labels = []

    for node in G.nodes:
        pos = layout[node]
        dot = Dot(point=pos, radius=node_radius)
        dots.append(dot)
        label = Text(str(node), font=font).scale(scale).next_to(dot, DOWN, buff=label_offset)
        labels.append(label)

    for u, v in G.edges:
        edge = Line(layout[u], layout[v], stroke_color=WHITE)
        lines.append(edge)

    return dots, lines, labels

def make_bar_chart(values, center=ORIGIN, width=0.3, spacing=0.4, max_height=2.5,
                   color=BLUE, opacity=0.8):
    """
    Creates a simple vertical bar chart from a list of numerical values.

    Args:
        values (list or np.array): The numerical values to plot.
        center (np.array): Center position of the chart.
        width (float): Width of each bar.
        spacing (float): Space between bars.
        max_height (float): Max bar height (scaled).
        color (Color): Fill color of bars.
        opacity (float): Opacity of bars.

    Returns:
        list: List of Rectangle objects representing bars.
    """
    bars = []
    max_val = max(values)
    n = len(values)

    for i, val in enumerate(values):
        h = val / max_val * max_height if max_val > 0 else 0.1
        bar = Rectangle(height=h, width=width, fill_color=color,
                        fill_opacity=opacity, stroke_width=0)
        bar.move_to(center + RIGHT * (i - n / 2 + 0.5) * spacing + UP * h / 2)
        bars.append(bar)

    return bars

# --- Animate node vibration in Laplacian mode ---
def vibrate_nodes(nodes, layout, norm_mode, t, amplitude=0.05):
    for i, node in enumerate(nodes):
        base = layout[i]
        amp = norm_mode[i]
        node.move_to(base + amplitude * amp * np.sin(2 * PI * t) * UP)

class WavyEdge(VMobject):
    def __init__(self, start_func, end_func, phase_tracker, amp=0.1, freq=4, samples=50, **kwargs):
        super().__init__(**kwargs)
        self.start_func = start_func
        self.end_func = end_func
        self.phase_tracker = phase_tracker
        self.amp = amp
        self.freq = freq
        self.samples = samples
        self.set_stroke(color=WHITE, width=2)

        self.add_updater(lambda m: m.update_wiggle())

    def update_wiggle(self):
        p1 = self.start_func()
        p2 = self.end_func()
        direction = p2 - p1
        length = np.linalg.norm(direction)
        unit = direction / length
        normal = np.cross(unit, OUT)

        points = []
        for i in range(self.samples + 1):
            t = i / self.samples
            wave = np.sin(self.freq * TAU * t + self.phase_tracker.get_value()) * self.amp
            point = p1 + unit * t * length + normal * wave
            points.append(point)

        self.set_points_as_corners(points)


def highlight_matrix_symmetry(matrix_mob):
    n = len(matrix_mob.get_rows())
    entries = matrix_mob.get_entries()

    def idx(i, j): return i * n + j

    for i in range(n):
        for j in range(n):
            entry = entries[idx(i, j)]
            if i == j:
                entry.set_color(YELLOW)
            elif i < j:
                entry.set_color(BLUE)
            else:
                entry.set_color(GREEN)

def pulse_circles(eigenvalues, center, spacing=0.6, scale=0.3, color=YELLOW):
    circles = []
    for i, eig in enumerate(eigenvalues):
        r = max(0.05, scale * eig)  # avoid zero radius
        x = center + RIGHT * (i - len(eigenvalues)/2) * spacing
        circle = Circle(radius=r, color=color)
        circle.move_to(x)
        circles.append(circle)
    return circles