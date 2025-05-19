from manimlib import *
from manimlib import ShowCreation

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.graph_utils import draw_graph, make_bar_chart, vibrate_nodes, highlight_matrix_symmetry, pulse_circles
from utils.graph_utils import WavyEdge

import numpy as np
import networkx as nx

# import math - not needed?

class GraphBasics(ThreeDScene):
    def construct(self):
        empty_text = Text("")
        empty_text.fix_in_frame()

        # ===================================================
        # GRAPH THEORY BASICS
        graph_theory_text = Text("Some Graph Theory basics", font_size=42)
        graph_theory_text.fix_in_frame()
        graph_theory_text.to_edge(UP, 0.2)

        self.play(ShowCreation(graph_theory_text, lag_ratio=0.01, run_time=0.5))
        self.play(FlashAround(graph_theory_text["Graph Theory"]), lag_ratio=0.01, run_time=0.5)
        self.play(graph_theory_text["Graph Theory"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)


        # ===================================================
        # GRAPHS NOT THESE
        graphs_not_text = Text("Graphs are not these", font_size=42)
        graphs_not_text.fix_in_frame()
        graphs_not_text.next_to(graph_theory_text, BOTTOM, 0.1)
        graphs_not_text.to_edge(LEFT, 1)

        self.play(ShowCreation(graphs_not_text, lag_ratio=0.01, run_time=0.5))
        self.play(FlashAround(graphs_not_text["Graphs"]), lag_ratio=0.01, run_time=0.5)
        self.play(graphs_not_text["Graphs"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        # ===================================================
        # CURVE
        square = Square3D(side_length = 3)
        curve_texture = "manim/img/curve1-front.png"

        square_surface = TexturedSurface(square, curve_texture)
        square_surface.mesh = SurfaceMesh(square_surface)
        square_surface.mesh.set_stroke(BLUE, 1, opacity=0.5)
        square_surface.add(square_surface.mesh)

        square_surface.next_to(graphs_not_text, BOTTOM, 0)
        square_surface.to_edge(LEFT, 2)

        self.play(
            FadeIn(square_surface),
            ShowCreation(square_surface.mesh, lag_ratio=0.01),
            run_time=0.5
        )

        self.play(
            Rotate(square_surface, - PI / 2, LEFT),
            run_time=0.5,
        )

        self.play(
            Rotate(square_surface, PI / 8, IN),
            run_time=0.5
        )

        # ===================================================
        # GRAPHS NOT THESE
        elliptic_curve_text = Text(
            """
            (in fact this is an
            'Elliptic Curve'...)
            """, font_size=36)
        elliptic_curve_text.fix_in_frame()
        elliptic_curve_text.next_to(square_surface, BOTTOM, 0.66)
        elliptic_curve_text.to_edge(LEFT, 1.5)

        self.play(ShowCreation(elliptic_curve_text, lag_ratio=0.01, run_time=0.5))
        self.play(FlashAround(elliptic_curve_text["Elliptic Curve"]), lag_ratio=0.01, run_time=0.5)
        self.play(elliptic_curve_text["Elliptic Curve"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        # ===================================================
        # COLLECTIONS OF NODES
        graphs_text = Text("They're collections of nodes", font_size=42)
        graphs_text.fix_in_frame()
        graphs_text.next_to(graph_theory_text, BOTTOM, 0.1)
        graphs_text.to_edge(RIGHT, 1)

        self.play(ShowCreation(graphs_text, lag_ratio=0.01, run_time=0.5))
        self.play(FlashAround(graphs_text["nodes"]), lag_ratio=0.01, run_time=0.5)
        self.play(graphs_text["nodes"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        # ===================================================
        # NODES
        axes = Axes((-3, 3), (-3, 3), unit_size=3)
        axes.next_to(graphs_text, BOTTOM, 0.33)
        axes.to_edge(RIGHT, 6.66)
        nodes = [
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
        ]

        nodes[0].move_to(axes.c2p(4.0, 2.0))
        nodes[1].move_to(axes.c2p(3.5, 2.5))
        nodes[2].move_to(axes.c2p(4.5, 2.5))
        nodes[3].move_to(axes.c2p(3.75, 3.0))
        nodes[4].move_to(axes.c2p(4.25, 3.0))

        for node in nodes:
            node.fix_in_frame()
            self.play(
                ShowCreation(node, lag_ratio=0.01),
                run_time=0.5
            )

        # ===================================================
        # CONNECTED IN SOME WAY
        connected_text = Text("Connected in...", font_size=42)
        connected_text.fix_in_frame()
        connected_text.next_to(nodes[0], BOTTOM, 0.1)

        self.play(ShowCreation(connected_text, lag_ratio=0.01, run_time=0.5))

        # ===================================================
        # CONNECTED IN SOME WAY
        some_way_text = Text("... some way", font_size=42)
        some_way_text.fix_in_frame()
        some_way_text.next_to(connected_text, BOTTOM, 0.05)

        self.play(ShowCreation(some_way_text, lag_ratio=0.01, run_time=0.5))
        self.play(FlashAround(some_way_text["some"]), lag_ratio=0.01, run_time=0.5)
        self.play(some_way_text["some"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        self.play(
            FadeOut(graph_theory_text),
            FadeOut(graphs_not_text),
            FadeOut(square_surface),
            FadeOut(elliptic_curve_text),
            FadeOut(graphs_text),
            FadeOut(connected_text),
            run_time=0.5,
        )

        # self.play(
        #     nodes[0].animate.fix_in_frame(),
        #     nodes[0].animate.move_to(ORIGIN),
        #     nodes[0].animate.to_edge(BOTTOM, 0.5),

        #     # nodes[1].animate.fix_in_frame(),
        #     # nodes[1].animate.next_to(nodes[0], RIGHT, 1.0),
        #     # # nodes[1].animate.to_edge(LEFT, 3.0),
            
        #     # nodes[2].animate.fix_in_frame(),
        #     # nodes[2].animate.next_to(nodes[0], LEFT, 1.0),
        #     # # nodes[2].animate.to_edge(RIGHT, 3.0),
            
        #     # nodes[3].animate.fix_in_frame(),
        #     # nodes[3].animate.next_to(nodes[0], TOP, 1.0),
        #     # # nodes[3].animate.to_edge(LEFT, 4.0),
        #     # # nodes[3].animate.next_to(nodes[1], RIGHT, 0.2),
            
        #     # nodes[4].animate.fix_in_frame(),
        #     # nodes[4].animate.next_to(nodes[0], TOP, 1.0),
        #     # # nodes[4].animate.to_edge(RIGHT, 4.0),
        #     # # nodes[4].animate.next_to(nodes[2], LEFT, 0.2)
        # )


class CompleteGraph(ThreeDScene):
    def construct(self):
        empty_text = Text("")
        empty_text.fix_in_frame()

        # ===================================================
        # COMPLETE GRAPH BASICS
        complete_graph_text = Text("The Complete Graph", font_size=42)
        complete_graph_text.fix_in_frame()
        complete_graph_text.to_edge(UP, 0.2)

        self.wait()

        self.play(Write(complete_graph_text, run_time=0.5)) # 1

        self.play(FlashAround(complete_graph_text["Complete"]), lag_ratio=0.01, run_time=0.5) # 2
        
        self.play(complete_graph_text["Complete"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 3

        # ===================================================
        # COMPLETE GRAPH DESCRIPTION
        complete_graph_description_text = Text(
            """The 'Complete Graph' is a Graph in which
            each node is connected, by an edge, to every other node
                                                        (except itself)""", font_size=42)
        complete_graph_description_text.fix_in_frame()
        complete_graph_description_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(Write(complete_graph_description_text, run_time=0.5)) # 4

        self.play(FlashAround(complete_graph_description_text["Graph"][1]), lag_ratio=0.01, run_time=0.5) # 5
        
        self.play(complete_graph_description_text["Graph"][1].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 6
        
        self.play(FlashAround(complete_graph_description_text["each node"]), lag_ratio=0.01, run_time=0.5) # 7
        
        self.play(complete_graph_description_text["each node"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 8
        
        self.play(FlashAround(complete_graph_description_text["edge"]), lag_ratio=0.01, run_time=0.5) # 9
        
        self.play(complete_graph_description_text["edge"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 10
        
        self.play(FlashAround(complete_graph_description_text["every other node"]), lag_ratio=0.01, run_time=0.5) # 11
        
        self.play(complete_graph_description_text["every other node"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 12
        
        self.play(FlashAround(complete_graph_description_text["except itself"], 1, 0, 4, RED), lag_ratio=0.01, run_time=0.5) # 13
        
        self.play(complete_graph_description_text["except itself"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 14
        

        self.wait()

        self.play(FadeOut(complete_graph_description_text), run_time=0.5) # 15
        

        # ===================================================
        # COMPLETE GRAPH NOTATION
        complete_graph_notation_text = Tex(
            R"\textsf{ The `Complete Graph' is usually denoted by the letter } \mathbb{K}",
            font_size=42
        )
        complete_graph_notation_text.fix_in_frame()
        complete_graph_notation_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(Write(complete_graph_notation_text, run_time=0.5)) # 16

        usually_denoted_text = complete_graph_notation_text["usually denoted"]
        self.play(FlashAround(usually_denoted_text), run_time=0.5) # 17
        self.play(usually_denoted_text.animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 18
        
        K_text = complete_graph_notation_text[R"\mathbb{K}"]
        self.play(FlashAround(K_text), run_time=0.5) # 19
        self.play(K_text.animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 20
        

        self.wait()


        K_n_text = Tex(
            R"\mathbb{K}_n \textsf{ has } n \textsf{ nodes }",
            font_size=42
        )
        K_n_text.fix_in_frame()
        K_n_text.next_to(complete_graph_notation_text, BOTTOM, 0.1)

        self.play(ShowCreation(K_n_text, lag_ratio=0.01, run_time=0.5)) # 21
        
        self.play(FadeOut(complete_graph_notation_text, lag_ratio=0.01, run_time=0.5)) # 22
        
        self.play(K_n_text.animate.next_to(complete_graph_text, BOTTOM, 0.1), lag_ratio=0.01, run_time=0.5) # 23
        

        self.wait()

        K_1_text = Tex(
            R"\mathbb{K}_1 \textsf{ has }  1 \textsf{ node }",
            font_size=42
        )
        K_1_text.fix_in_frame()
        K_1_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(ReplacementTransform(K_n_text, K_1_text, lag_ratio=0.01, run_time=0.5)) # 24
        

        nodes = [
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
        ]
        num_nodes = len(nodes)
        M_adjacency = str(num_nodes)
        print(M_adjacency)

        for node in nodes:
            node.fix_in_frame()

        nodes[0].move_to(ORIGIN)
        self.play(ShowCreation(nodes[0], lag_ratio=0.01, run_time=0.5)) # 25
        

        self.wait()

        trivial_text = Text("(but this is the trivial case)", font_size=32)
        trivial_text.fix_in_frame()
        trivial_text.next_to(K_1_text, BOTTOM, 0.1)

        self.play(ShowCreation(trivial_text, lag_ratio=0.01, run_time=0.5)) # 26
        
        self.play(FlashAround(trivial_text["trivial"]), lag_ratio=0.01, run_time=0.5) # 27
        
        self.play(trivial_text["trivial"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 28
        

        self.wait()

        K_2_text = Tex(
            R"\mathbb{K}_2 \textsf{ has }  2 \textsf{ nodes }",
            font_size=42
        )
        K_2_text.fix_in_frame()
        K_2_text.next_to(complete_graph_text, BOTTOM, 0.1)
        self.play(ReplacementTransform(K_1_text, K_2_text, lag_ratio=0.01, run_time=0.5)) # 29

        self.play(FadeOut(trivial_text, lag_ratio=0.01, run_time=0.5)) # 30

        nodes[1].next_to(nodes[0], BOTTOM, 0.3)

        self.play(ShowCreation(nodes[1], lag_ratio=0.01, run_time=0.5)) # 31

        self.wait()

        K_2_connected_text = Text("and they are connected to each other, by an edge", font_size=32)
        K_2_connected_text.fix_in_frame()
        K_2_connected_text.next_to(K_1_text, BOTTOM, 0.1)

        self.play(ShowCreation(K_2_connected_text, lag_ratio=0.01, run_time=0.5)) # 32
        
        self.play(FlashAround(K_2_connected_text["connected"]), lag_ratio=0.01, run_time=0.5) # 33
        
        self.play(K_2_connected_text["connected"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 34
        
        self.play(FlashAround(K_2_connected_text["by an edge"]), lag_ratio=0.01, run_time=0.5) # 35
        
        self.play(K_2_connected_text["by an edge"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 36
        

        edges = [
            [
                None,
                Line(nodes[0], nodes[1]),
                Line(nodes[0], nodes[2]),
                Line(nodes[0], nodes[3]),
                Line(nodes[0], nodes[4]),
            ],
            [
                None,
                None,
                Line(nodes[1], nodes[2]),
                Line(nodes[1], nodes[3]),
                Line(nodes[1], nodes[4]),
            ],
            [
                None,
                None,
                None,
                Line(nodes[2], nodes[3]),
                Line(nodes[2], nodes[4]),
            ],
            [
                None,
                None,
                None,
                None,
                Line(nodes[3], nodes[4]),
            ],
        ]

        # def update_edges(nodes, edges)
        list_count = 0
        for edge_list in edges:
            edge_count = 0
            for edge in edge_list:
                if (edge != None):
                    edge.fix_in_frame()
                    always(edges[list_count][edge_count].set_start_and_end_attrs, nodes[list_count], nodes[edge_count])
                edge_count = edge_count + 1
            list_count = list_count + 1
        
        self.play(ShowCreation(edges[0][1], lag_ratio=0.01, run_time=0.5)) # 37
        

        # self.play(nodes[0].animate.set_x(1), lag_ratio=0.01, run_time=0.5)


class AlignOnCircle(Scene):
    def construct(self):
        # Create the big circle
        big_circle = Circle(radius=2, color=WHITE)
        self.play(ShowCreation(big_circle))

        # Suppose you want 6 small circles around the big circle
        n = 6
        small_circles = [
            Circle(radius=0.15, color=BLUE).set_fill(BLUE, opacity=0.5)
            for _ in range(n)
        ]

        # Define an updater so each small circle keeps to a fixed angle
        for i, sc in enumerate(small_circles):
            angle = 2 * PI * i / n

            # This updater re-positions the small circle on big_circle's circumference
            def updater_func(mobj, angle=angle):
                center = big_circle.get_center()
                radius = big_circle.get_radius()
                offset = np.array([np.cos(angle), np.sin(angle), 0]) * radius
                mobj.move_to(center + offset)

            sc.add_updater(updater_func)

            # Put it in the correct place initially
            updater_func(sc)
            self.add(sc)

        self.wait(1)

        # Now any transformations on 'big_circle' will keep the small circles on its circumference:
        self.play(big_circle.animate.shift(LEFT*2), run_time=2)
        self.wait(0.5)
        self.play(big_circle.animate.scale(1.5), run_time=2)
        self.wait(1)



class GraphGeneralisationTest(ThreeDScene):
    def construct(self):
        # STRUCTURE CIRCLE
        node_structure_circle = Circle(0, GREEN, radius=2.0)
        node_structure_circle.fix_in_frame()
        node_structure_circle.set_stroke(opacity=0)
        node_structure_circle.set_fill(opacity=0)

        structure_circle_spin_angle = 0

        # NODE INITIALISE
        num_nodes = 5 # must be positive integer
        node_colour = YELLOW
        node_radius = 0.3
        nodes = [
            Circle(0, node_colour, radius=node_radius)
            for _ in range(num_nodes)
        ]
        nodes_names = [
            Text(str(i+1), font_size=42)
            for i in range(num_nodes)
        ]

        # Define an UPDATER so NODE keeps to CIRCUMFERENCE
        # Keep NODE NAMES in place as well
        for i, node in enumerate(nodes):
            node.fix_in_frame()
            nodes_names[i].fix_in_frame()
            angle = (2 * PI * i / num_nodes) + (PI / 2)

            # This updater re-positions the small circle on big_circle's circumference
            def node_updater_func(mobj, angle=angle, i=i):
                full_angle = angle + structure_circle_spin_angle

                center = node_structure_circle.get_center()
                radius = node_structure_circle.get_radius()
                offset = np.array([np.cos(full_angle), np.sin(full_angle), 0]) * radius

                # Put node where it should be
                mobj.move_to(center + offset)

                # Put node name where it should be
                nodes_names[i].move_to(mobj, ORIGIN)

                # edges_row = edges[i]
                # for j, edge in enumerate(edges_row):
                #     edges[i][j].set_start_and_end_attrs(nodes[i], nodes[j])


            # add updater func to each node
            node.add_updater(node_updater_func)

            # Put it in the correct place initially
            node_updater_func(node, angle)

        # EDGES INITIALISE
        complete_adj_matrix = complete_graph_adjacency(num_nodes)

        edges = []
        # ... turn values in adj matrix into array of edges (lines)
        for i, row in enumerate(complete_adj_matrix): # i is the row number
            edges_row = []
            for j, field_in_row in enumerate(row): # j is the column number
                # assuming you can't have a node pointing to itself...
                # we only care about 
                if (j > i):
                    if field_in_row == 1:
                        # make a line between node i and j
                        new_edge = Line(nodes[i], nodes[j], 0)
                        new_edge.fix_in_frame()
                        edges_row.append(new_edge)

            edges.append(edges_row)
        
        # SHOW INITIAL NODES / NAMES / EDGES
        for node in nodes:
            self.play(ShowCreation(node), run_time=0.5)

        for node_name in nodes_names:
            self.play(ShowCreation(node_name), run_time=0.5)
        
        for edge_row in edges: # get a row
            for edge in edge_row: # get the edge in a field of the row
                self.play(ShowCreation(edge), run_time=0.5)
                
        # NOW - MOVE THINGS AROUND AS YOU LIKE!!!
        self.play(node_structure_circle.animate.shift(LEFT*2), run_time=2)
        self.wait(0.5)
        self.play(node_structure_circle.animate.scale(1.5), run_time=2)
        self.wait(0.5)

        circle_divisions = 180
        epsilon = (2 * PI) / circle_divisions
        for i in range(circle_divisions):
            structure_circle_spin_angle += epsilon
            # self.play(node_structure_circle.animate.rotate(PI/10,about_point=node_structure_circle.get_center()),lag_ratio=0.0001,run_time=0.0001)
            # self.play()
            self.update_frame(0, True)


        self.wait(0.5)
        self.play(node_structure_circle.animate.scale(0.666), run_time=2)
        self.wait(0.5)



class FundamentalGraphs(ThreeDScene):
    def construct(self):
        # empty_text = Text("")
        # empty_text.fix_in_frame()

        # intro_text1 = Text("So first of all...")
        # intro_text1.fix_in_frame()
        # intro_text1.to_edge(UP)
        # self.play(
        #     ShowCreation(intro_text1, lag_ratio=0.01, run_time=0.5)
        # )
        square = Square3D(side_length = 6)
        curve_texture = "/manim/img/curve1-front.png"

        surfaces = [
            TexturedSurface(surface, curve_texture)
            for surface in [square]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01),
            run_time=3
        )
        for mob in surfaces:
            mob.add(mob.mesh)


# FUNCTIONS

def complete_graph_adjacency(n):
    M = np.ones((n, n), dtype=int)  # Create an n×n matrix of 1s
    np.fill_diagonal(M, 0)         # Set diagonal entries to 0
    return M

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()

# Slide (3) - What Does a Graph Sound Like?
# make run-scene SCENE=CompareSpectraScene
# make render-scene SCENE=CompareSpectraScene
class CompareSpectraScene(Scene):
    def construct(self):
        # --- Step 1: Define Graphs ---
        G1 = nx.path_graph(4)
        G2 = nx.star_graph(3)

        layout1 = nx.spring_layout(G1, seed=42)
        layout2 = nx.spring_layout(G2, seed=8)

        layout1 = {k: 3 * np.append(p, 0) + LEFT * 3.5 + UP * 1 for k, p in layout1.items()}
        layout2 = {k: 3 * np.append(p, 0) + RIGHT * 3.5 + UP * 1 for k, p in layout2.items()}

        # --- Step 2: Draw Graphs ---
        g1_dots, g1_edges, g1_labels = draw_graph(G1, layout1)
        g2_dots, g2_edges, g2_labels = draw_graph(G2, layout2)

        self.play(*[ShowCreation(e) for e in g1_edges + g2_edges], run_time=1.2)
        self.play(*[FadeIn(d) for d in g1_dots + g2_dots], run_time=0.6)
        self.play(*[FadeIn(l) for l in g1_labels + g2_labels], run_time=0.6)
        self.wait(0.3)

        # --- Step 3: Show Spectra ---
        L1 = nx.laplacian_matrix(G1).toarray()
        L2 = nx.laplacian_matrix(G2).toarray()
        eigs1 = np.round(np.linalg.eigvalsh(L1), 2)
        eigs2 = np.round(np.linalg.eigvalsh(L2), 2)

        bars1 = make_bar_chart(eigs1, center=ORIGIN + LEFT * 4 + DOWN * 3)
        bars2 = make_bar_chart(eigs2, center=ORIGIN + RIGHT * 4 + DOWN * 3)

        self.play(*[FadeIn(b) for b in bars1 + bars2], run_time=1)
        self.wait(0.3)

        # --- Step 4: Highlight G1 (Path) ---
        label1 = Text("Path Graph").set_color(YELLOW).scale(1).to_corner(UL).shift(DOWN * 0.6)
        self.play(FadeIn(label1))
        self.play(*[Indicate(d, color=YELLOW, scale_factor=2) for d in g1_dots], run_time=1.2)
        for i in range(1, 4):  # Adjust number of tones if needed
            self.play(Indicate(bars1[i], color=YELLOW), run_time=1.2)
            self.wait(0.6)
        self.wait(0.3)
        self.play(*[Indicate(b, color=YELLOW, scale_factor=1.5) for b in bars1], run_time=1.2)
        self.wait(0.3)
        self.play(FadeOut(label1))

        # --- Step 5: Highlight G2 (Star) ---
        label2 = Text("Star Graph").set_color(GREEN).scale(1).to_corner(UR).shift(DOWN * 0.6)
        self.play(FadeIn(label2))
        self.play(*[Indicate(d, color=GREEN, scale_factor=2) for d in g2_dots], run_time=1.2)
        for i in range(1, 4):  # Adjust number of tones if needed
            self.play(Indicate(bars2[i], color=GREEN), run_time=1.2)
            self.wait(0.6)
        self.wait(0.3)
        self.play(*[Indicate(b, color=GREEN, scale_factor=1.5) for b in bars2], run_time=1.2)
        self.wait(0.3)
        self.play(FadeOut(label2))

        self.play(*[Indicate(b, color=YELLOW, scale_factor=1.5) for b in bars1], run_time=1.2)
        self.wait(0.3)
        self.play(*[Indicate(b, color=GREEN, scale_factor=1.5) for b in bars2], run_time=1.2)
        self.wait(0.3)
        self.play(*[Indicate(b, color=YELLOW, scale_factor=1.5) for b in bars1], run_time=1.2)
        self.wait(0.3)
        self.play(*[Indicate(b, color=GREEN, scale_factor=1.5) for b in bars2], run_time=1.2)
        self.wait(0.3)

        self.wait(10)

# class CompareSpectraWithSound(Scene):
#     def construct(self):
#         # Graphs
#         G1 = nx.path_graph(4)
#         G2 = nx.star_graph(3)

#         layout1 = nx.spring_layout(G1, seed=42)
#         layout2 = nx.spring_layout(G2, seed=8)
#         layout1 = {k: 3 * np.append(p, 0) + LEFT * 3.5 + UP * 1 for k, p in layout1.items()}
#         layout2 = {k: 3 * np.append(p, 0) + RIGHT * 3.5 + UP * 1 for k, p in layout2.items()}

#         g1_dots, g1_edges, g1_labels = draw_graph(G1, layout1)
#         g2_dots, g2_edges, g2_labels = draw_graph(G2, layout2)

#         self.play(*[ShowCreation(e) for e in g1_edges + g2_edges])
#         self.play(*[FadeIn(d) for d in g1_dots + g2_dots])
#         self.play(*[FadeIn(l) for l in g1_labels + g2_labels])

#         self.wait(0.5)
#         self.add_sound("./audio/graph1.wav")
#         for _ in range(3):
#             self.play(*[Indicate(d, color=YELLOW) for d in g1_dots], run_time=0.5)

#         self.wait(0.5)
#         self.add_sound("./audio/graph2.wav")
#         for _ in range(3):
#             self.play(*[Indicate(d, color=GREEN) for d in g2_dots], run_time=0.5)

#         self.wait()


class CompareSpectraWithSound(Scene):
    def construct(self):
        # Graph definitions
        G1 = nx.path_graph(4)
        G2 = nx.star_graph(3)

        layout1 = nx.spring_layout(G1, seed=42)
        layout2 = nx.spring_layout(G2, seed=8)
        layout1 = {k: 3 * np.append(p, 0) + LEFT * 3.5 + UP for k, p in layout1.items()}
        layout2 = {k: 3 * np.append(p, 0) + RIGHT * 3.5 + UP for k, p in layout2.items()}

        # Draw both graphs
        g1_dots, g1_edges, g1_labels = draw_graph(G1, layout1)
        g2_dots, g2_edges, g2_labels = draw_graph(G2, layout2)

        self.play(*[ShowCreation(e) for e in g1_edges + g2_edges])
        self.play(*[FadeIn(d) for d in g1_dots + g2_dots])
        self.play(*[FadeIn(l) for l in g1_labels + g2_labels])
        self.wait(0.5)

        # Add sequential tones for Graph 1
        for i in range(1, 4):  # Adjust number of tones if needed
            try:
                sound_path = Path(f"sounds/path4_tone{i}.mp3").resolve()
                self.add_sound(str(sound_path))
                self.play(*[Indicate(d, color=YELLOW) for d in g1_dots], run_time=1.2)
            except FileNotFoundError:
                break

        self.wait(0.5)

        # Add sequential tones for Graph 2
        for i in range(1, 4):  # Adjust number of tones if needed
            try:
                sound_path = Path(f"./sounds/star3_tone{i}.mp3").resolve()
                self.add_sound(str(sound_path))
                self.play(*[Indicate(d, color=GREEN) for d in g2_dots], run_time=1.2)
            except FileNotFoundError:
                break

        self.wait(0.5)

        # Optional: play both chords together
        sound_path = Path(f"./sounds/path4_chord.wav").resolve()
        self.add_sound(sound_path, time_offset=0)
        sound_path = Path(f"./sounds/star3_chord.wav").resolve()
        self.add_sound(sound_path, time_offset=0)
        self.play(
            *[Indicate(d, color=BLUE) for d in g1_dots + g2_dots],
            run_time=2
        )

        self.wait()


# Slide (4) - Why Study Spectra?
# make run-scene FLAGS='-r "1440x1080"' SCENE=VibratingGraphScene
# make render-scene FLAGS='-r "1440x1080"' SCENE=VibratingGraphScene
class VibratingGraphScene(Scene):
    def construct(self):
        # --- Graph Setup: Cycle graph C3 (triangle) ---
        G = nx.cycle_graph(3)
        layout = nx.spring_layout(G, seed=1)
        layout = {k: 2 * np.append(p, 0) for k, p in layout.items()}

        # --- Eigenmode: Get 2nd Laplacian eigenvector ---
        L = nx.laplacian_matrix(G).toarray()
        eigvals, eigvecs = np.linalg.eigh(L)
        mode = eigvecs[:, 1]  # first non-zero mode
        max_amp = max(abs(mode))
        norm_mode = mode / max_amp

        # --- Draw Nodes ---
        nodes = [Dot(point=layout[i], radius=0.1) for i in G.nodes]
        for node in nodes:
            self.add(node)

        # --- Edge Wiggle Animation Setup ---
        phase = ValueTracker(0)

        # --- Create animated wavy edges ---
        for u, v in G.edges:
            edge = WavyEdge(
                start_func=lambda u=u: nodes[u].get_center(),
                end_func=lambda v=v: nodes[v].get_center(),
                phase_tracker=phase,
                amp=0.05,
                freq=4
            )
            self.add(edge)

        # Combine vibration + edge wiggle
        self.play(
            UpdateFromAlphaFunc(VGroup(*nodes), lambda m, alpha: vibrate_nodes(nodes, layout, norm_mode, alpha * 10)),
            phase.animate.increment_value(400 * PI),
            run_time=12
        )

        self.wait()

        # === Step: Fade out vibrating triangle ===
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1)
        self.wait(0.5)

        # === Step: Build more complex graph ===
        G2 = nx.erdos_renyi_graph(10, 0.3, seed=2)  # random but connected-ish
        layout_start = nx.spring_layout(G2, seed=2)
        layout_end = nx.circular_layout(G2)

        layout_start = {k: 3 * np.append(p, 0) for k, p in layout_start.items()}
        layout_end = {k: 3 * np.append(p, 0) for k, p in layout_end.items()}

        # Create nodes and edges
        nodes2 = [Dot(point=layout_start[i], radius=0.1, color=WHITE) for i in G2.nodes]
        labels2 = []
        for i in G2.nodes:
            label = Text(str(i), font='Consolas', stroke_width=0).scale(0.3)
            label.add_updater(lambda m, i=i: m.next_to(nodes2[i], DOWN, buff=0.1))
            labels2.append(label)
        
        edges2 = []
        for u, v in G2.edges:
            line = Line(layout_start[u], layout_start[v], color=WHITE)
            line.add_updater(lambda m, u=u, v=v: m.put_start_and_end_on(
                nodes2[u].get_center(), nodes2[v].get_center()))
            edges2.append(line)

        self.play(
            *[ShowCreation(e) for e in edges2],
            *[FadeIn(n) for n in nodes2],
            *[FadeIn(l) for l in labels2],
            run_time=2
        )
        self.wait(0.5)

        # === Step: Morph to different layout ===
        for i, node in enumerate(nodes2):
            self.play(node.animate.move_to(layout_end[i]), run_time=0.5)

        self.wait(10)


# Slide (5) - The Graph Laplacian
# make run-scene SCENE=GraphLaplacianScene
# make render-scene SCENE=GraphLaplacianScene
class GraphLaplacianScene(Scene):
    def construct(self):
        # --- Step 1: Graph Setup ---
        G = nx.path_graph(4)
        layout = nx.spring_layout(G, seed=5)
        layout = {k: 2.5 * np.append(p, 0) + LEFT * 4 for k, p in layout.items()}

        # Draw graph
        dots = [Dot(point=layout[i], radius=0.1) for i in G.nodes]
        edges = [Line(layout[u], layout[v]) for u, v in G.edges]
        labels = [Text(str(i)).scale(0.4).next_to(dots[i], DOWN, buff=0.15) for i in G.nodes]

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], lag_ratio=0, run_time=0.2)
        self.play(*[FadeIn(l) for l in labels], lag_ratio=0, run_time=0.2)

        # --- Step 2: Adjacency Matrix ---
        A = nx.adjacency_matrix(G).todense()
        A_mtx = Matrix(A).scale(0.6).to_edge(UP).shift(RIGHT * 3)
        A_label = Text("A = Adjacency", font_size=24).next_to(A_mtx, DOWN, buff=0.2)

        self.play(Write(A_mtx), lag_ratio=0, run_time=1)
        self.play(FadeIn(A_label), lag_ratio=0, run_time=1)

        # --- Step 3: Degree Matrix ---
        degrees = np.diag([G.degree[i] for i in G.nodes])
        D_mtx = Matrix(degrees).scale(0.6).next_to(A_mtx, LEFT, buff=1.2)
        D_label = Text("D = Degree", font_size=24).next_to(D_mtx, DOWN, buff=0.2)

        self.play(Write(D_mtx), lag_ratio=0, run_time=1)
        self.play(FadeIn(D_label), lag_ratio=0, run_time=1)

        # --- Step 4: Laplacian Matrix ---
        L = degrees - A
        L_mtx = Matrix(L).scale(0.6).next_to(A_mtx, DOWN, buff=1.2)
        L_label = Text("L = D - A (Laplacian)", font_size=24).next_to(L_mtx, DOWN, buff=0.4)

        self.play(TransformFromCopy(D_mtx, L_mtx), lag_ratio=0, run_time=1)
        self.play(L_mtx.animate.shift(DOWN * 0.2), lag_ratio=0, run_time=1)
        self.play(FadeIn(L_label), lag_ratio=0, run_time=1)

        # --- Step 5: Highlight Symmetry ---
        symm_text = Text("Symmetric ⇒ always real eigenvalues", font_size=24).next_to(L_label, DOWN)
        norm_label = Tex(r"L_{\text{norm}} = I - T^{-1/2} A T^{-1/2}").scale(0.7)
        norm_label.next_to(symm_text, DOWN, buff=0.6)
        self.play(Write(norm_label))
        self.wait(0.5)
        highlight_matrix_symmetry(D_mtx)
        highlight_matrix_symmetry(A_mtx)
        highlight_matrix_symmetry(L_mtx)
        self.play(FadeIn(symm_text), lag_ratio=0, run_time=1)

        # --- Step 6: Pulse an Eigenmode ---
        eigvals, eigvecs = np.linalg.eigh(L)
        mode = eigvecs[:, 1]  # second smallest (first non-zero)
        max_amp = max(abs(mode))
        norm_mode = mode / max_amp

        self.play(
            UpdateFromAlphaFunc(VGroup(*dots), lambda m, alpha: vibrate_nodes(dots, layout, norm_mode, alpha * 2, amplitude=0.2)),
            run_time=2
        )

        self.wait(10)

# Slide (6) - Spectral Fingerprints in the Zoo
# make run-scene SCENE=GraphZooScene
# make render-scene SCENE=GraphZooScene
class GraphZooScene(Scene):
    def construct(self):
        graphs = [
            ("Path", nx.path_graph(8)),
            ("Star", nx.star_graph(7)),
            ("Complete", nx.complete_graph(8)),
            ("Cycle", nx.cycle_graph(8)),
            ("Hypercube", nx.hypercube_graph(3)),
            ("Cartesian", nx.cartesian_product(nx.path_graph(4), nx.path_graph(2))),
        ]

        positions = [
            UL, UP, UR,
            DL, DOWN, DR,
        ]

        graph_mobs = []
        for (label, G), pos in zip(graphs, positions):
            layout = nx.spring_layout(G, seed=1)
            layout = {k: np.append(p, 0) + pos*2 for k, p in layout.items()}
            dots, edges, _ = draw_graph(G, layout)
            group = VGroup(*edges, *dots)
            graph_mobs.append((label, G, group.scale(0.5), layout))

        # Show all graphs in layout
        self.play(*[FadeIn(group) for _, _, group, _ in graph_mobs], run_time=1)

        caption = Text("     Each graph has a unique spectral fingerprint\n(each 'animal' here has 8 nodes ⇒ an 8x8 Laplacian)").scale(0.6).to_edge(DOWN)
        self.play(FadeIn(caption))

        i = 0
        for label, G, group, layout in graph_mobs:
            # Zoom into graph
            self.play(group.animate.scale(1.5).move_to(ORIGIN), run_time=1)

            # Compute and display Laplacian
            L = nx.laplacian_matrix(G).toarray()
            eigs = np.round(np.linalg.eigvalsh(L), 2)

            L_mtx = Matrix(L).scale(0.5).to_corner(UL)
            L_lbl = Text(f"{label} Graph Laplacian").scale(0.5).next_to(L_mtx, DOWN)
            bars = make_bar_chart(eigs, center=RIGHT * 4 + UP * 0.5)
            pulses = pulse_circles(eigs, center=DOWN * 2)

            self.play(Write(L_mtx), FadeIn(L_lbl), run_time=0.5)
            self.play(*[FadeIn(b) for b in bars], run_time=0.5)
            self.play(*[FadeIn(p) for p in pulses], run_time=0.5)

            # Pulse animation
            for _ in range(2):
                self.play(*[Indicate(p, scale_factor=1.5) for p in pulses], run_time=1)

            # Clear everything except collage
            self.play(
                FadeOut(L_mtx), FadeOut(L_lbl),
                *[FadeOut(b) for b in bars],
                *[FadeOut(p) for p in pulses],
                group.animate.scale(1/1.5).move_to(positions[i] * 2)  # move back out
            )
            i += 1
            self.wait(0.2)

        self.wait(10)

# Demo - Spectral Intuition
# make run-scene SCENE=SpectralIntuitionScene
# make render-scene SCENE=SpectralIntuitionScene

# class SpectralIntuitionScene(Scene):
#     def construct(self):
#         graph_types = [
#             ("Path", nx.path_graph(6)),
#             ("Star", nx.star_graph(5)),
#             ("Complete", nx.complete_graph(6)),
#             # add Cycle, Hypercube, etc. later
#         ]

#         positions = {
#             "Path": LEFT * 4 + UP,
#             "Star": ORIGIN + UP,
#             "Complete": RIGHT * 4 + UP
#         }

#         for name, G in graph_types:
#             layout = nx.spring_layout(G, seed=42)
#             layout = {k: 2.5 * np.append(p, 0) + positions[name] for k, p in layout.items()}

#             # Step 1: draw graph
#             dots, edges, labels = draw_graph(G, layout)

#             self.play(*[ShowCreation(e) for e in edges], run_time=1)
#             self.play(*[FadeIn(d) for d in dots], run_time=1)
#             self.play(*[FadeIn(l) for l in labels], run_time=1)

#             # Step 2: highlight distances from node 0
#             node0 = 0
#             distances = nx.single_source_shortest_path_length(G, node0)
#             for i in sorted(set(distances.values())):
#                 group = [k for k, d in distances.items() if d == i]
#                 self.play(*[Indicate(dots[k], color=[YELLOW, GREEN, BLUE, RED][i]) for k in group], run_time=1)

#             # Step 3: show spectrum as bar chart
#             L = nx.laplacian_matrix(G).toarray()
#             eigs = np.round(np.linalg.eigvalsh(L), 2)
#             bars = make_bar_chart(eigs, center=positions[name] + DOWN * 2.5)
#             self.play(*[FadeIn(b) for b in bars], run_time=1)

#             self.wait(1)

#             # Optional: fade out or keep all for final side-by-side
#             self.play(*[FadeOut(m) for m in dots + edges + labels + bars], run_time=0.5)

        # Final wrap-up (e.g. fade in side-by-side summary or titles)


# Demo - Spectral Intuition - Path Graph
# make run-scene SCENE=SpectralIntuition
# make render-scene SCENE=SpectralIntuition
class SpectralIntuition(Scene):
    def construct(self):
        # --- Step 0: define graphs ---
        graphs = [
            ("Path", nx.path_graph(8)),
            ("Star", nx.star_graph(7)),
            ("Complete", nx.complete_graph(8)),
            ("Cycle", nx.cycle_graph(8)),
            ("Hypercube", nx.hypercube_graph(3)),
            ("Cartesian", nx.cartesian_product(nx.path_graph(4), nx.path_graph(2))),
        ]

        captions = [
            "No short-cuts. Always increasing distance / eigenvalues",
            "2 steps to get (n-2) other nodes (6 small eigenvalues), only 1 step to get to central node",
            "Everything is 1 step away. All Eigenvalues equal",
            "2 distinct ways to get to anything. Eigenvalues in pairs",
            "3 distinct ways to move from any corner... the eigenvalues are in triplets",
            "2 or 3 ways to start from any node... then paths start to 'overlap'... gets 'messy'"
        ]

        text_mobs = []
        arrow_mobs = []

        # --- Step 1.1: Define and layout graph (Path P6) ---
        G = graphs[0][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 3 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 1.2: Highlight distances from node 0 ---
        node0 = 0
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            self.play(*[Indicate(dots[n], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 1.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 1.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(len(walk_order) - 1):
            u = walk_order[i]
            v = walk_order[i + 1]
            edge = Line(layout[u], layout[v], color=walk_colors[i], stroke_width=6)
            colour_edges.append(edge)

            # Replace original edge with coloured one
            self.play(ShowCreation(edge), run_time=0.3)

            # Highlight the node arrived at
            self.play(Indicate(dots[v], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if i + 1 < len(bar_chart):
                self.play(bar_chart[i + 1].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 1.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 1.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + LEFT * 6.3 + UP * 2.8
        chart_target_pos = graph_target_pos + RIGHT * 1.5

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[0], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, RIGHT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        # ================================================================================
        # ================================================================================
        # ================================================================================
        # ================================================================================

        # --- Step 2.1: Define and layout graph (Path P6) ---
        G = graphs[1][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 2 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 2.2: Highlight distances from node 0 ---
        node0 = 0
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            self.play(*[Indicate(dots[n], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 2.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 2.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(len(walk_order) - 1):
            u = 0
            v = walk_order[i + 1]
            edge = Line(layout[u], layout[v], color=walk_colors[i], stroke_width=6)
            colour_edges.append(edge)

            # Replace original edge with coloured one
            self.play(ShowCreation(edge), run_time=0.3)

            # Highlight the node arrived at
            self.play(Indicate(dots[v], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if i + 1 < len(bar_chart):
                self.play(bar_chart[i + 1].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 2.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 2.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + LEFT * 6.0 + UP * 1.0
        chart_target_pos = graph_target_pos + RIGHT * 1.5

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[1], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, RIGHT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        # ================================================================================
        # ================================================================================
        # ================================================================================
        # ================================================================================

        # --- Step 3.1: Define and layout graph (Path P6) ---
        G = graphs[2][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 2 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 3.2: Highlight distances from node 0 ---
        node0 = 0
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            self.play(*[Indicate(dots[n], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 3.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 3.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(len(walk_order)):
            for j in range(len(walk_order)):
                if i != j:
                    u = i
                    v = j
                    edge = Line(layout[i], layout[j], color=walk_colors[i], stroke_width=6)
                    colour_edges.append(edge)

                    # Replace original edge with coloured one
                    self.play(ShowCreation(edge), run_time=0.1)

            # Highlight the node arrived at
            # self.play(Indicate(dots[v], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if i + 1 < len(bar_chart):
                self.play(bar_chart[i + 1].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 3.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 3.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + LEFT * 6.0 + DOWN * 1.0
        chart_target_pos = graph_target_pos + RIGHT * 1.5

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[2], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, RIGHT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        # ================================================================================
        # ================================================================================
        # ================================================================================
        # ================================================================================

        # --- Step 4.1: Define and layout graph (Path P6) ---
        G = graphs[3][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 2 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 4.2: Highlight distances from node 0 ---
        node0 = 0
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            self.play(*[Indicate(dots[n], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 4.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 4.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, RED]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(math.ceil(len(walk_order) / 2)):
            u_1 = walk_order[(0 + i)] # leave 0 in to mod arithmetic clearer
            v_1 = walk_order[(0 + i + 1)] # leave 0 in to mod arithmetic clearer
            u_2 = walk_order[(8 - i) % 8]
            v_2 = walk_order[(8 - i - 1) % 8]
            edge_1 = Line(layout[u_1], layout[v_1], color=walk_colors[i], stroke_width=6)
            edge_2 = Line(layout[u_2], layout[v_2], color=walk_colors[i], stroke_width=6)
            colour_edges.append(edge_1)
            colour_edges.append(edge_2)

            # Replace original edge with coloured one
            self.play(ShowCreation(edge_1), run_time=0.3)
            self.play(ShowCreation(edge_2), run_time=0.3)

            # Highlight the node arrived at
            self.play(Indicate(dots[v_1], color=walk_colors[i], scale_factor=2), run_time=0.2)
            self.play(Indicate(dots[v_2], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if ((2 * i + 1) < len(bar_chart)):
                self.play(bar_chart[2 * i + 1].animate.set_color(walk_colors[i]), run_time=0.3)
            if ((2 * i + 2) < len(bar_chart)):
                self.play(bar_chart[2 * i + 2].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 4.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 4.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + LEFT * 6.0 + DOWN * 3
        chart_target_pos = graph_target_pos + RIGHT * 1.5

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[3], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, RIGHT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        # ================================================================================
        # ================================================================================
        # ================================================================================
        # ================================================================================

        # --- Step 5.1: Define and layout graph (Path P6) ---
        G = graphs[4][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 2 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 5.2: Highlight distances from node 0 ---
        node0 = (0, 0, 0)
        # print(G)
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            # print(group)
            # print(dots)
            self.play(*[Indicate(dots[1], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 5.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 5.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, RED]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(math.ceil(len(walk_order) / 2)):
            u_1 = walk_order[(0 + i)] # leave 0 in to mod arithmetic clearer
            v_1 = walk_order[(0 + i + 1)] # leave 0 in to mod arithmetic clearer
            u_2 = walk_order[(8 - i) % 8]
            v_2 = walk_order[(8 - i - 1) % 8]
            # edge_1 = Line(layout[u_1], layout[v_1], color=walk_colors[i], stroke_width=6)
            # edge_2 = Line(layout[u_2], layout[v_2], color=walk_colors[i], stroke_width=6)
            # colour_edges.append(edge_1)
            # colour_edges.append(edge_2)

            # Replace original edge with coloured one
            # self.play(ShowCreation(edge_1), run_time=0.3)
            # self.play(ShowCreation(edge_2), run_time=0.3)

            # Highlight the node arrived at
            self.play(Indicate(dots[v_1], color=walk_colors[i], scale_factor=2), run_time=0.2)
            self.play(Indicate(dots[v_2], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if ((2 * i + 1) < len(bar_chart)):
                self.play(bar_chart[2 * i + 1].animate.set_color(walk_colors[i]), run_time=0.3)
            if ((2 * i + 2) < len(bar_chart)):
                self.play(bar_chart[2 * i + 2].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 5.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 5.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + RIGHT * 6.0 + UP * 2.0,
        chart_target_pos = graph_target_pos + LEFT * 2.0

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[4], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, LEFT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        # ================================================================================
        # ================================================================================
        # ================================================================================
        # ================================================================================

        # --- Step 6.1: Define and layout graph (Path P6) ---
        G = graphs[5][1]
        layout = nx.spring_layout(G, seed=2)
        layout = {k: 3 * np.append(p, 0) + LEFT * 2 for k, p in layout.items()}

        # --- Draw nodes, edges, labels ---
        dots, edges, labels = draw_graph(G, layout)

        self.play(*[ShowCreation(e) for e in edges], run_time=1)
        self.play(*[FadeIn(d) for d in dots], run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.5)

        # --- Step 6.2: Highlight distances from node 0 ---
        node0 = (0, 0)
        print(G)
        distances = nx.single_source_shortest_path_length(G, node0)
        colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

        for d in range(max(distances.values()) + 1):
            group = [n for n, dist in distances.items() if dist == d]
            self.play(*[Indicate(dots[1], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

        # --- Step 6.3: Show Laplacian spectrum ---
        L = nx.laplacian_matrix(G).toarray()
        eigs = np.round(np.linalg.eigvalsh(L), 2)

        spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
        bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

        self.play(FadeIn(spectrum_caption), run_time=0.4)
        self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

        # --- Step 6.4: Walk from node 0 and colour edges + bars ---
        walk_colors = [YELLOW, GREEN, GOLD, RED]
        walk_order = [0, 1, 2, 3, 4, 5, 6, 7]

        colour_edges = []
        for i in range(math.ceil(len(walk_order) / 2)):
            u_1 = walk_order[(0 + i)] # leave 0 in to mod arithmetic clearer
            v_1 = walk_order[(0 + i + 1)] # leave 0 in to mod arithmetic clearer
            u_2 = walk_order[(8 - i) % 8]
            v_2 = walk_order[(8 - i - 1) % 8]
            # edge_1 = Line(layout[u_1], layout[v_1], color=walk_colors[i], stroke_width=6)
            # edge_2 = Line(layout[u_2], layout[v_2], color=walk_colors[i], stroke_width=6)
            # colour_edges.append(edge_1)
            # colour_edges.append(edge_2)

            # Replace original edge with coloured one
            # self.play(ShowCreation(edge_1), run_time=0.3)
            # self.play(ShowCreation(edge_2), run_time=0.3)

            # Highlight the node arrived at
            self.play(Indicate(dots[v_1], color=walk_colors[i], scale_factor=2), run_time=0.2)
            self.play(Indicate(dots[v_2], color=walk_colors[i], scale_factor=2), run_time=0.2)

            # Highlight the corresponding bar
            if ((2 * i + 1) < len(bar_chart)):
                self.play(bar_chart[2 * i + 1].animate.set_color(walk_colors[i]), run_time=0.3)
            if ((2 * i + 2) < len(bar_chart)):
                self.play(bar_chart[2 * i + 2].animate.set_color(walk_colors[i]), run_time=0.3)

        self.wait()

        # --- Step 6.5: Fade out the "Laplacian Eigenvalues" label ---
        self.play(FadeOut(spectrum_caption), run_time=0.5)

        # --- Step 6.6: Shrink and move graph + bar chart to top-left corner ---
        graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
        chart_group = VGroup(*bar_chart)

        self.play(
            graph_group.animate.scale(0.3),
            chart_group.animate.scale(0.3),
            run_time=0.5
        )

        graph_target_pos = ORIGIN + RIGHT * 6.0 + DOWN * 2.0,
        chart_target_pos = graph_target_pos + LEFT * 1.5

        self.play(
            graph_group.animate.move_to(graph_target_pos),
            chart_group.animate.move_to(chart_target_pos),
            run_time=1
        )
        self.wait(0.5)

        # Add explanation text and arrow
        text = Text(captions[5], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
        text.next_to(chart_target_pos, LEFT, buff=0.5)
        # arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
        # self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
        self.play(FadeIn(text), run_time=0.6)
        text_mobs.append(text)
        # arrow_mobs.append(arrow)
        self.wait(0.5)

        self.wait(10)


class SpectralIntuition_New(Scene):
    def construct(self):
        graphs = [
            ("Path", nx.path_graph(8)),
            ("Star", nx.star_graph(7)),
            ("Complete", nx.complete_graph(8)),
            ("Cycle", nx.cycle_graph(8)),
            ("Hypercube", nx.hypercube_graph(3)),
            ("Cartesian", nx.cartesian_product(nx.path_graph(4), nx.path_graph(2))),
        ]

        positions = [
            ORIGIN + LEFT * 6.3 + UP * 2.8,
            ORIGIN + LEFT * 6.0 + UP * 1.0,
            ORIGIN + LEFT * 6.0 + DOWN * 1.0,
            ORIGIN + LEFT * 6.0 + DOWN * 3,
            ORIGIN + RIGHT * 6.0 + UP * 2.0,
            ORIGIN + RIGHT * 6.0 + DOWN * 2.0
        ]

        captions = [
            "No short-cuts. Always increasing distance / eigenvalues",
            "2 steps to get (n-2) other nodes (6 small eigenvalues), only 1 step to get to central node",
            "Everything is 1 step away. All Eigenvalues equal",
            "2 distinct ways to get to anything. Eigenvalues in pairs",
            "3 distinct ways to move from any corner... then it gets 'messy'",
            "2 or 3 ways to start from any node... then paths start to 'overlap'... gets 'messy' again"
        ]

        text_mobs = []
        arrow_mobs = []

        for i, (name, G) in enumerate(graphs):
            layout = nx.spring_layout(G, seed=2)
            layout = {k: 3 * np.append(p, 0) for k, p in layout.items()}

            dots, edges, labels = draw_graph(G, layout)
            L = nx.laplacian_matrix(G).toarray()
            eigs = np.round(np.linalg.eigvalsh(L), 2)

            spectrum_caption = Text("Laplacian Eigenvalues", font_size=28).next_to(ORIGIN + RIGHT * 3.5 + UP * 1.5, DOWN)
            bar_chart = make_bar_chart(eigs, center=ORIGIN + RIGHT * 3.5)

            self.play(*[ShowCreation(e) for e in edges], run_time=1)
            self.play(*[FadeIn(d) for d in dots], run_time=0.5)
            self.play(*[FadeIn(l) for l in labels], run_time=0.5)

            distances = nx.single_source_shortest_path_length(G, 0)
            colour_map = [YELLOW, GREEN, GOLD, BLUE, RED, TEAL, ORANGE, LIGHT_PINK]

            for d in range(max(distances.values()) + 1):
                group = [n for n, dist in distances.items() if dist == d]
                self.play(*[Indicate(dots[n], color=colour_map[d % len(colour_map)], scale_factor=2) for n in group], run_time=0.2)

            self.play(FadeIn(spectrum_caption), run_time=0.4)
            self.play(*[FadeIn(b) for b in bar_chart], run_time=0.4)

            # Simple placeholder walk logic (could customise later)
            walk_order = list(G.nodes)
            colour_edges = []
            for j in range(len(walk_order) - 1):
                u, v = walk_order[j], walk_order[j + 1]
                edge = Line(layout[u], layout[v], color=colour_map[j % len(colour_map)], stroke_width=6)
                colour_edges.append(edge)
                self.play(ShowCreation(edge), run_time=0.2)
                self.play(Indicate(dots[v], color=colour_map[j % len(colour_map)], scale_factor=2), run_time=0.2)
                if j + 1 < len(bar_chart):
                    self.play(bar_chart[j + 1].animate.set_color(colour_map[j % len(colour_map)]), run_time=0.3)

            self.play(FadeOut(spectrum_caption), run_time=0.5)
            graph_group = VGroup(*dots, *edges, *labels, *colour_edges)
            chart_group = VGroup(*bar_chart)

            self.play(graph_group.animate.scale(0.3), chart_group.animate.scale(0.3), run_time=0.5)
            graph_target_pos = positions[i]
            chart_target_pos = graph_target_pos + RIGHT * 1.5

            self.play(graph_group.animate.move_to(graph_target_pos), chart_group.animate.move_to(chart_target_pos), run_time=1)
            self.wait(0.5)

            # Add explanation text and arrow
            text = Text(captions[i], font_size=24, t2c={"short-cuts": YELLOW, "eigenvalues": TEAL})
            text.next_to(graph_target_pos, LEFT if i < 4 else RIGHT, buff=0.5)
            arrow = Arrow(text.get_right(), graph_target_pos, buff=0.1) if i < 4 else Arrow(text.get_left(), graph_target_pos, buff=0.1)
            self.play(FadeIn(text), ShowCreation(arrow), run_time=0.6)
            text_mobs.append(text)
            arrow_mobs.append(arrow)

        self.wait(1)



from manimlib import *

class LaplacianSubtractionAnimated(Scene):
    def construct(self):
        # --- Degree matrix D ---
        D = Matrix([
            [7, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ]).scale(0.45)

        # --- Adjacency matrix A ---
        A = Matrix([
            [0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]).scale(0.45)

        # --- Target Laplacian matrix ---
        L = Matrix([
            [7, -1, -1, -1, -1, -1, -1, -1],
            [-1, 1, 0, 0, 0, 0, 0, 0],
            [-1, 0, 1, 0, 0, 0, 0, 0],
            [-1, 0, 0, 1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 1, 0, 0, 0],
            [-1, 0, 0, 0, 0, 1, 0, 0],
            [-1, 0, 0, 0, 0, 0, 1, 0],
            [-1, 0, 0, 0, 0, 0, 0, 1],
        ]).scale(0.45)

        # --- Positioning ---
        D.move_to(LEFT * 4)
        A.next_to(D, RIGHT, buff=1)
        L.next_to(A, RIGHT, buff=1)

        minus = Tex("-").scale(2).next_to(D, RIGHT, buff=0.2)
        equals = Tex("=").scale(2).next_to(A, RIGHT, buff=0.2)

        # --- Labels ---
        title = Text("Laplacian as D - A", font_size=40).to_edge(UP)

        # --- Step 1: Intro objects ---
        self.play(Write(title))
        self.play(Write(D), Write(minus), Write(A), Write(equals))

        # --- Step 2: Animate subtraction entry-by-entry ---
        D_entries = D.get_entries()
        A_entries = A.get_entries()
        L_entries = L.get_entries()

        animations = []
        for i in range(len(D_entries)):
            # Convert to number values
            d_val = D_entries[i]
            a_val = A_entries[i]
            l_val = L_entries[i]

            # Highlight and transform
            highlight = SurroundingRectangle(d_val, color=YELLOW, buff=0.05)
            highlight2 = SurroundingRectangle(a_val, color=BLUE, buff=0.05)

            max_time = 0.5
            min_time = 0.001
            time_diff = max_time - min_time
            time_step = time_diff / len(D_entries)
            run_time = max_time - (time_step * i) + min_time

            self.play(ShowCreation(highlight), ShowCreation(highlight2), run_time=run_time**3) # run_time cubed to maake it drop fast towards 0
            self.play(TransformFromCopy(d_val, l_val), run_time=run_time**3)
            self.remove(highlight, highlight2)

        # Fade in final matrix
        self.play(FadeIn(L))

        # Optional: Flash rows or show L = D - A caption again
        self.play(Indicate(L), run_time=0.5)

        # --- Step 3: Fade everything except Laplacian and move it left ---
        self.play(
            FadeOut(D), FadeOut(A), FadeOut(minus), FadeOut(equals), FadeOut(title),
            L.animate.to_edge(LEFT * 1.5).scale(0.9),
            run_time=1
        )
        self.wait(0.5)

        # --- Step 4: Define eigenvector ψ = δ₂ - δ₃ ---
        psi_vector = Matrix([
            [0],
            [1],
            [-1],
            [0],
            [0],
            [0],
            [0],
            [0]
        ]).scale(0.6).next_to(L, RIGHT, buff=1)

        psi_label = Tex(r"\psi = \delta_2 - \delta_3").scale(0.8).next_to(psi_vector, UP)
        eq_label = Tex(r"L \cdot \psi = ?").scale(0.8).next_to(psi_vector, RIGHT, buff=0.8)

        self.play(Write(psi_vector), FadeIn(psi_label), Write(eq_label))
        self.wait(1)

        # --- Step 5: Highlight row-by-row dot products ---
        result_entries = []

        for row_idx in range(8):
            row = L.get_rows()[row_idx]
            highlight_row = SurroundingRectangle(row, color=YELLOW, buff=0.05)
            highlights_col = []

            # get matching ψ entries that are nonzero
            for col_idx, entry in enumerate(psi_vector.get_entries()):
                try:
                    val = float(entry.get_tex())
                except ValueError:
                    val = 0.0
                if val != 0.0:
                    highlights_col.append(SurroundingRectangle(entry, color=BLUE, buff=0.05))

            self.play(ShowCreation(highlight_row), *[ShowCreation(h) for h in highlights_col], run_time=0.4)

            # Compute dot product manually
            L_row_vals = []
            for e in L.get_rows()[row_idx]:
                try:
                    L_row_vals.append(int(e.get_tex()))
                except ValueError:
                    L_row_vals.append(0)

            ψ_vals = []
            for e in psi_vector.get_entries():
                try:
                    ψ_vals.append(int(e.get_tex()))
                except ValueError:
                    ψ_vals.append(0)
            result = sum(L_row_vals[i] * ψ_vals[i] for i in range(len(ψ_vals)))

            result_entry = Integer(result).scale(0.6)
            result_entry.move_to(L.get_rows()[row_idx].get_right() + RIGHT * 3.5)

            self.play(FadeIn(result_entry), run_time=0.3)
            result_entries.append(result_entry)

            self.play(FadeOut(highlight_row), *[FadeOut(h) for h in highlights_col])

        self.wait(0.5)

        # --- Step 6: Show conclusion ---
        lambda_val = Integer(1).scale(0.6)
        equals_vec = Matrix([
            [0],
            [1],
            [-1],
            [0],
            [0],
            [0],
            [0],
            [0]
        ]).scale(0.6).next_to(result_entries[0], RIGHT, buff=1)

        self.play(
            FadeIn(lambda_val),
            lambda_val.animate.next_to(result_entries[0], LEFT, buff=0.2),
            FadeIn(equals_vec),
            run_time=1
        )

        equals_label = Tex(r"= \lambda \cdot \psi").scale(0.8).next_to(equals_vec, RIGHT)
        self.play(FadeIn(equals_label))
        self.wait(1)
