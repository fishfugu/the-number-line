from manim import *
from manimlib import *
from manimlib import ShowCreation

class GraphBasics(ThreeDScene):
    def construct(self):
        empty_text = Text("")
        empty_text.fix_in_frame()

        # ===================================================
        # GRAPH THEORY BASICS
        graph_theory_text = Text("Some Graph Theory basics", font_size=42)
        graph_theory_text.fix_in_frame()
        graph_theory_text.to_edge(UP, 0.2)

        self.play(ShowCreation(graph_theory_text, lag_ratio=0.01, run_time=2))
        self.play(FlashAround(graph_theory_text["Graph Theory"]), lag_ratio=0.01, run_time=1)
        self.play(graph_theory_text["Graph Theory"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)


        # ===================================================
        # GRAPHS NOT THESE
        graphs_not_text = Text("Graphs are not these", font_size=42)
        graphs_not_text.fix_in_frame()
        graphs_not_text.next_to(graph_theory_text, BOTTOM, 0.1)
        graphs_not_text.to_edge(LEFT, 1)

        self.play(ShowCreation(graphs_not_text, lag_ratio=0.01, run_time=2))
        self.play(FlashAround(graphs_not_text["Graphs"]), lag_ratio=0.01, run_time=1)
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
            run_time=1
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

        self.play(ShowCreation(elliptic_curve_text, lag_ratio=0.01, run_time=2))
        self.play(FlashAround(elliptic_curve_text["Elliptic Curve"]), lag_ratio=0.01, run_time=1)
        self.play(elliptic_curve_text["Elliptic Curve"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        # ===================================================
        # COLLECTIONS OF NODES
        graphs_text = Text("They're collections of nodes", font_size=42)
        graphs_text.fix_in_frame()
        graphs_text.next_to(graph_theory_text, BOTTOM, 0.1)
        graphs_text.to_edge(RIGHT, 1)

        self.play(ShowCreation(graphs_text, lag_ratio=0.01, run_time=2))
        self.play(FlashAround(graphs_text["nodes"]), lag_ratio=0.01, run_time=1)
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

        self.play(ShowCreation(connected_text, lag_ratio=0.01, run_time=1))

        # ===================================================
        # CONNECTED IN SOME WAY
        some_way_text = Text("... some way", font_size=42)
        some_way_text.fix_in_frame()
        some_way_text.next_to(connected_text, BOTTOM, 0.05)

        self.play(ShowCreation(some_way_text, lag_ratio=0.01, run_time=1))
        self.play(FlashAround(some_way_text["some"]), lag_ratio=0.01, run_time=1)
        self.play(some_way_text["some"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5)

        self.play(
            FadeOut(graph_theory_text),
            FadeOut(graphs_not_text),
            FadeOut(square_surface),
            FadeOut(elliptic_curve_text),
            FadeOut(graphs_text),
            FadeOut(connected_text),
            run_time=1,
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

        self.play(Write(complete_graph_text, run_time=2)) # 1

        self.play(FlashAround(complete_graph_text["Complete"]), lag_ratio=0.01, run_time=1) # 2
        
        self.play(complete_graph_text["Complete"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=1) # 3

        # ===================================================
        # COMPLETE GRAPH DESCRIPTION
        complete_graph_description_text = Text(
            """The 'Complete Graph' is a Graph in which
            each node is connected, by an edge, to every other node
                                                        (except itself)""", font_size=42)
        complete_graph_description_text.fix_in_frame()
        complete_graph_description_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(Write(complete_graph_description_text, run_time=2)) # 4

        self.play(FlashAround(complete_graph_description_text["Graph"][1]), lag_ratio=0.01, run_time=1) # 5
        
        self.play(complete_graph_description_text["Graph"][1].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 6
        
        self.play(FlashAround(complete_graph_description_text["each node"]), lag_ratio=0.01, run_time=1) # 7
        
        self.play(complete_graph_description_text["each node"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 8
        
        self.play(FlashAround(complete_graph_description_text["edge"]), lag_ratio=0.01, run_time=1) # 9
        
        self.play(complete_graph_description_text["edge"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 10
        
        self.play(FlashAround(complete_graph_description_text["every other node"]), lag_ratio=0.01, run_time=1) # 11
        
        self.play(complete_graph_description_text["every other node"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 12
        
        self.play(FlashAround(complete_graph_description_text["except itself"], 1, 0, 4, RED), lag_ratio=0.01, run_time=1) # 13
        
        self.play(complete_graph_description_text["except itself"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 14
        

        self.wait()

        self.play(FadeOut(complete_graph_description_text), run_time=1) # 15
        

        # ===================================================
        # COMPLETE GRAPH NOTATION
        complete_graph_notation_text = Tex(
            R"\textsf{ The `Complete Graph' is usually denoted by the letter } \mathbb{K}",
            font_size=42
        )
        complete_graph_notation_text.fix_in_frame()
        complete_graph_notation_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(Write(complete_graph_notation_text, run_time=1)) # 16

        usually_denoted_text = complete_graph_notation_text["usually denoted"]
        self.play(FlashAround(usually_denoted_text), run_time=1) # 17
        self.play(usually_denoted_text.animate.set_color(TEAL_A), lag_ratio=0.01, run_time=1) # 18
        
        K_text = complete_graph_notation_text[R"\mathbb{K}"]
        self.play(FlashAround(K_text), run_time=1) # 19
        self.play(K_text.animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 20
        

        self.wait()


        K_n_text = Tex(
            R"\mathbb{K}_n \textsf{ has } n \textsf{ nodes }",
            font_size=42
        )
        K_n_text.fix_in_frame()
        K_n_text.next_to(complete_graph_notation_text, BOTTOM, 0.1)

        self.play(ShowCreation(K_n_text, lag_ratio=0.01, run_time=1)) # 21
        
        self.play(FadeOut(complete_graph_notation_text, lag_ratio=0.01, run_time=1)) # 22
        
        self.play(K_n_text.animate.next_to(complete_graph_text, BOTTOM, 0.1), lag_ratio=0.01, run_time=1) # 23
        

        self.wait()

        K_1_text = Tex(
            R"\mathbb{K}_1 \textsf{ has }  1 \textsf{ node }",
            font_size=42
        )
        K_1_text.fix_in_frame()
        K_1_text.next_to(complete_graph_text, BOTTOM, 0.1)

        self.play(ReplacementTransform(K_n_text, K_1_text, lag_ratio=0.01, run_time=1)) # 24
        

        nodes = [
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
            Circle(0, YELLOW, radius=0.1),
        ]
        num_nodes = len(nodes)
        M_adjacency = complete_graph_adjacency(num_nodes)
        print(M_adjacency)

        for node in nodes:
            node.fix_in_frame()

        nodes[0].move_to(ORIGIN)
        self.play(ShowCreation(nodes[0], lag_ratio=0.01, run_time=1)) # 25
        

        self.wait()

        trivial_text = Text("(but this is the trivial case)", font_size=32)
        trivial_text.fix_in_frame()
        trivial_text.next_to(K_1_text, BOTTOM, 0.1)

        self.play(ShowCreation(trivial_text, lag_ratio=0.01, run_time=1)) # 26
        
        self.play(FlashAround(trivial_text["trivial"]), lag_ratio=0.01, run_time=1) # 27
        
        self.play(trivial_text["trivial"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 28
        

        self.wait()

        K_2_text = Tex(
            R"\mathbb{K}_2 \textsf{ has }  2 \textsf{ nodes }",
            font_size=42
        )
        K_2_text.fix_in_frame()
        K_2_text.next_to(complete_graph_text, BOTTOM, 0.1)
        self.play(ReplacementTransform(K_1_text, K_2_text, lag_ratio=0.01, run_time=1)) # 29

        self.play(FadeOut(trivial_text, lag_ratio=0.01, run_time=1)) # 30

        nodes[1].next_to(nodes[0], BOTTOM, 0.3)

        self.play(ShowCreation(nodes[1], lag_ratio=0.01, run_time=1)) # 31

        self.wait()

        K_2_connected_text = Text("and they are connected to each other, by an edge", font_size=32)
        K_2_connected_text.fix_in_frame()
        K_2_connected_text.next_to(K_1_text, BOTTOM, 0.1)

        self.play(ShowCreation(K_2_connected_text, lag_ratio=0.01, run_time=1)) # 32
        
        self.play(FlashAround(K_2_connected_text["connected"]), lag_ratio=0.01, run_time=1) # 33
        
        self.play(K_2_connected_text["connected"].animate.set_color(TEAL_A), lag_ratio=0.01, run_time=0.5) # 34
        
        self.play(FlashAround(K_2_connected_text["by an edge"]), lag_ratio=0.01, run_time=1) # 35
        
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
        
        self.play(ShowCreation(edges[0][1], lag_ratio=0.01, run_time=1)) # 37
        

        # self.play(nodes[0].animate.set_x(1), lag_ratio=0.01, run_time=1)



class FundamentalGraphs(ThreeDScene):
    def construct(self):
        # empty_text = Text("")
        # empty_text.fix_in_frame()

        # intro_text1 = Text("So first of all...")
        # intro_text1.fix_in_frame()
        # intro_text1.to_edge(UP)
        # self.play(
        #     ShowCreation(intro_text1, lag_ratio=0.01, run_time=2)
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
