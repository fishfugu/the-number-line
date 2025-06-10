from manimlib import *
from manimlib import ShowCreation

import sys
import os

import numpy as np
import networkx as nx


class QSqrt2VectorSpace(Scene):
    def construct(self):
        # Define axes manually (since Axes is different in ManimGL)
        axes = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(0.8)

        axes.add_coordinate_labels(
            font_size=12,
            num_decimal_places=0
        )
        axes_labels = VGroup(
            Text("1").scale(0.3).next_to(axes.x_axis.get_end(), RIGHT),
            Tex("\\sqrt{2}").scale(0.4).next_to(axes.y_axis.get_end(), UP)
        )

        self.play(ShowCreation(axes), FadeIn(axes_labels))

        # Plot lattice of a + b√2
        points = VGroup()
        labels = VGroup()

        for a in range(-3, 4):
            for b in range(-3, 4):
                dot = Dot(axes.c2p(a, b), radius=0.03, color=YELLOW)
                label = Tex(f"{a} + {b}\\sqrt{{2}}").scale(0.1).next_to(dot, UR, buff=0.1)
                points.add(dot)
                labels.add(label)

        self.play(LaggedStartMap(FadeIn, points, lag_ratio=0.03))
        self.play(LaggedStartMap(Write, labels, lag_ratio=0.04))

        # Highlight basis vectors
        basis_1 = Arrow(axes.c2p(0, 0), axes.c2p(1, 0), buff=0, color=RED, fill_color=RED, fill_opacity=1)
        basis_sqrt2 = Arrow(axes.c2p(0, 0), axes.c2p(0, 1), buff=0, color=GREEN, fill_color=GREEN, fill_opacity=1)
        basis_1_plus_2sqrt2 = Arrow(axes.c2p(0, 0), axes.c2p(1, 2), buff=0, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        basis_label_1 = Tex("1").scale(0.3).set_color(RED).next_to(basis_1.get_end(), DOWN, buff=0.1)
        basis_label_sqrt2 = Tex("\\sqrt{2}").scale(0.3).set_color(GREEN).next_to(basis_sqrt2.get_end(), LEFT, buff=0.1)
        basis_label_1_plus_2sqrt2 = Tex("1 + 2 \\sqrt{2}").scale(0.3).set_color(YELLOW).next_to(basis_1_plus_2sqrt2.get_end(), DR, buff=0.1)

        self.play(GrowArrow(basis_1), Write(basis_label_1))
        self.play(GrowArrow(basis_sqrt2), Write(basis_label_sqrt2))
        self.play(GrowArrow(basis_1_plus_2sqrt2), Write(basis_label_1_plus_2sqrt2))

        self.wait(2)


class FirstIsomorphismTheoremScene(Scene):
    def construct(self):
        # Title
        title = Text("First Isomorphism Theorem").scale(1.5)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        # Group G elements
        g_labels = [r"g_1", r"g_2", r"g_3", r"g_4", r"g_5", r"g_6"]
        g_elems = VGroup(*[Dot() for _ in g_labels])
        g_elems.next_to(title, DOWN, buff=0.6)
        g_elems.arrange(RIGHT, buff=2).shift(1.5*UP)
        g_texts = VGroup(*[Tex(label).next_to(dot, UP) for dot, label in zip(g_elems, g_labels)])
        G_label = Tex(r"\text{Group } G").next_to(title, DOWN, buff=0.3)

        # Group H elements
        h_labels = [r"h_1", r"h_2", r"h_3"]
        h_elems = VGroup(*[Dot() for _ in h_labels])
        h_elems.arrange(RIGHT, buff=4).shift(2*DOWN)
        h_texts = VGroup(*[Tex(label).next_to(dot, DOWN) for dot, label in zip(h_elems, h_labels)])
        H_label = Tex(r"\text{Group } H").next_to(h_texts, DOWN, buff=0.3)

        # Display G and H
        self.play(FadeIn(G_label), FadeIn(H_label))
        self.play(LaggedStartMap(FadeIn, g_elems), LaggedStartMap(Write, g_texts))
        self.play(LaggedStartMap(FadeIn, h_elems), LaggedStartMap(Write, h_texts))

        # Homomorphism arrows (grouping elements mapping to same image)
        arrows = VGroup(
            Arrow(g_elems[0], h_elems[0], buff=0.1),
            Arrow(g_elems[1], h_elems[0], buff=0.1),
            Arrow(g_elems[2], h_elems[1], buff=0.1),
            Arrow(g_elems[3], h_elems[1], buff=0.1),
            Arrow(g_elems[4], h_elems[2], buff=0.1),
            Arrow(g_elems[5], h_elems[2], buff=0.1),
        )
        self.play(LaggedStartMap(GrowArrow, arrows))

        # Group the cosets of the kernel
        coset_circles = VGroup(
            SurroundingRectangle(VGroup(g_elems[0], g_elems[1]), color=BLUE),
            SurroundingRectangle(VGroup(g_elems[2], g_elems[3]), color=GREEN),
            SurroundingRectangle(VGroup(g_elems[4], g_elems[5]), color=RED),
        )
        coset_labels = VGroup(
            Tex(r"g_1 \ker(\varphi)").scale(0.8).next_to(coset_circles[0], UP).set_color(BLUE),
            Tex(r"g_3 \ker(\varphi)").scale(0.8).next_to(coset_circles[1], UP).set_color(GREEN),
            Tex(r"g_5 \ker(\varphi)").scale(0.8).next_to(coset_circles[2], UP).set_color(RED),
        )

        self.play(ShowCreation(coset_circles[0]), FadeIn(coset_labels[0]))
        self.play(ShowCreation(coset_circles[1]), FadeIn(coset_labels[1]))
        self.play(ShowCreation(coset_circles[2]), FadeIn(coset_labels[2]))

        self.wait(1)

        # Transform G to G/ker(phi)
        g_quotient_dots = VGroup(
            Dot().move_to(g_elems[0].get_center()).set_color(BLUE),
            Dot().move_to(g_elems[2].get_center()).set_color(GREEN),
            Dot().move_to(g_elems[4].get_center()).set_color(RED),
        )
        quotient_labels = VGroup(
            Tex(r"g_1 \ker(\varphi)").next_to(g_quotient_dots[0], UP).set_color(BLUE),
            Tex(r"g_3 \ker(\varphi)").next_to(g_quotient_dots[1], UP).set_color(GREEN),
            Tex(r"g_5 \ker(\varphi)").next_to(g_quotient_dots[2], UP).set_color(RED),
        )
        Gq_label = Tex(r"\text{Quotient Group} G / \ker(\varphi)").next_to(g_quotient_dots, UP, buff=1.5).move_to(G_label.get_center())

        self.play(
            FadeOut(g_elems),
            FadeOut(g_texts),
            FadeOut(coset_circles),
            ReplacementTransform(coset_labels, quotient_labels),
            FadeIn(g_quotient_dots),
            FadeOut(H_label),
            ReplacementTransform(G_label, Gq_label),
        )

        # Show arrows from quotient group to H
        quotient_arrows = VGroup(
            Arrow(g_quotient_dots[0], h_elems[0], buff=0.1).set_color(BLUE),
            Arrow(g_quotient_dots[1], h_elems[1], buff=0.1).set_color(GREEN),
            Arrow(g_quotient_dots[2], h_elems[2], buff=0.1).set_color(RED),
        )
        self.play(
            LaggedStartMap(GrowArrow, quotient_arrows),
            FadeOut(arrows),
        )

        self.wait(1)

        # Final isomorphism statement
        iso_eq = Tex(r"G / \ker(\varphi) \cong \mathrm{im}(\varphi)").scale(1.2).to_edge(DOWN)
        self.play(Write(iso_eq))
        self.wait(2)


class PrimaryToInvariantDecomposition(Scene):
    def construct(self):
        # Title
        title = Text("Relating Primary and Invariant Factor Decompositions").scale(1)
        title.to_edge(UP)
        self.play(Write(title))

        # Step 1: Show example group in primary form
        primary_eq = Tex(r"G \cong \mathbb{Z}_{4} \times \mathbb{Z}_{2} \times \mathbb{Z}_{9} \times \mathbb{Z}_{3}")
        primary_eq.shift(2.5*UP)
        self.play(Write(primary_eq))

        # Step 2: Show grouping by prime
        z4 = Rectangle(color=BLUE).scale(0.5).shift(LEFT*5 + UP*0.5)
        z2 = Rectangle(color=BLUE).scale(0.5).next_to(z4, RIGHT, buff=0.8)

        z3 = Rectangle(color=GREEN).scale(0.5).shift(RIGHT*5 + UP*0.5)
        z9 = Rectangle(color=GREEN).scale(0.5).next_to(z3, LEFT, buff=0.8)

        z_labels = VGroup(
            Tex(r"\mathbb{Z}_4").scale(0.7).move_to(z4.get_center()),
            Tex(r"\mathbb{Z}_2").scale(0.7).move_to(z2.get_center()),
            Tex(r"\mathbb{Z}_9").scale(0.7).move_to(z9.get_center()),
            Tex(r"\mathbb{Z}_3").scale(0.7).move_to(z3.get_center()),
        )

        boxes = VGroup(z4, z2, z9, z3)
        self.play(
            FadeIn(boxes), 
            Write(z_labels)
        )

        # Step 3: Group blue and green blocks
        brace2 = Brace(VGroup(z4, z2), DOWN, buff=0.2)
        brace3 = Brace(VGroup(z9, z3), DOWN, buff=0.2)
        label2 = brace2.get_tex(r"2\text{-primary part}")
        label3 = brace3.get_tex(r"3\text{-primary part}")

        self.play(GrowFromCenter(brace2), Write(label2))
        self.play(GrowFromCenter(brace3), Write(label3))

        # Step 4: Combine using structure theorem
        combined_2 = Tex(r"\mathbb{Z}_4 \times \mathbb{Z}_2 \cong \mathbb{Z}_8").scale(0.9).next_to(brace2, UP, buff=1.5)
        combined_3 = Tex(r"\mathbb{Z}_9 \times \mathbb{Z}_3 \cong \mathbb{Z}_{27}").scale(0.9).next_to(brace3, UP, buff=1.5)
        self.play(TransformFromCopy(VGroup(z4, z2), combined_2))
        self.play(TransformFromCopy(VGroup(z9, z3), combined_3))

        # Step 5: Rearrange into invariant factor form
        inv_eq = Tex(r"G \cong \mathbb{Z}_8 \times \mathbb{Z}_{27}").scale(1.1).shift(2.5*DOWN)
        arrow_2 = Arrow(combined_2.get_bottom() + DOWN*0.1 + RIGHT*0.1, inv_eq.get_top() + UP*0.1 + LEFT*0.3, buff=0.1).set_color(BLUE)
        arrow_3 = Arrow(combined_3.get_bottom() + DOWN*0.1 + LEFT*0.5, inv_eq.get_top() + UP*0.1 + RIGHT*0.9, buff=0.1).set_color(GREEN)
        self.play(
            GrowArrow(arrow_2),
            GrowArrow(arrow_3),
            Write(inv_eq),
        )

        self.play(combined_2.animate.set_color(BLUE))
        self.play(combined_3.animate.set_color(GREEN))

        # inv_eq_2_highlight = inv_eq.get_part_by_tex("\mathbb{Z}_8")
        # self.play(inv_eq_2_highlight.animate.set_color(BLUE))

        # inv_eq_3_highlight = inv_eq.get_part_by_tex(r"\mathbb{Z}_{27}")
        # self.play(inv_eq.animate.set_color(GREEN))

        # Step 6: Summary
        summary = Tex(r"\text{Primary} \Rightarrow \text{Invariant Factor}").scale(1).to_edge(DOWN)
        self.play(Write(summary))


class ModularWindowShift(Scene):
    def construct(self):
        title = Text("Modular Arithmetic as a Sliding Window").to_edge(UP, buff=0.5)
        imagine = Tex(r"\text{Imagine steping from 0 to 14 ...}").next_to(title, BOTTOM, buff=0.05)
        imagine_mod = Tex(r"\text{... but doing it `mod 7'}").next_to(imagine, BOTTOM, buff=0.05)

        self.play(Write(title))
        self.play(Write(imagine))
        self.play(Write(imagine_mod))

        # Step 1: Draw number line with [0, 7)
        number_line = NumberLine(x_range=(-2,15,1), unit_size=0.7, include_numbers=True)
        self.play(ShowCreation(number_line))

        mod_points = [0, 7, 14]
        arrows = VGroup()

        for val in mod_points:
            arrow = Arrow(
                end=number_line.number_to_point(val) + UP * 0.7,
                start=number_line.number_to_point(val) + UP * 0.5,
                stroke_color=RED,
                stroke_width=5,
            )
            arrows.add(arrow)

        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.5))

        # Bracket from 0 to 7
        window_bracket = Brace(number_line).scale(0.39).move_to(number_line.number_to_point((0+7)/2) + LEFT*0.2 + DOWN*0.6)
        window_label = window_bracket.get_tex(r"0 \leq x < 7")
        self.play(GrowFromCenter(window_bracket), Write(window_label))

        # Step 2: Animate modular wrap-around
        moving_dot = Dot().move_to(number_line.number_to_point(0)).set_color(YELLOW)
        self.play(FadeIn(moving_dot))

        positions = [1, 2, 3, 4, 5, 6, 0]  # Show wrap at 7 -> 0
        for val in positions:
            self.play(ApplyMethod(moving_dot.move_to, number_line.number_to_point(val)), run_time=0.5)
        for val in positions:
            self.play(ApplyMethod(moving_dot.move_to, number_line.number_to_point(val)), run_time=0.5)
        self.play(FadeOut(moving_dot))

        self.play(FadeOut(imagine), run_time=0.2)
        self.play(FadeOut(imagine_mod), run_time=0.2)

        imagine = Tex(r"\text{Now slide that window up to start at 5 ...}").next_to(title, BOTTOM, buff=0.05)
        imagine_mod = Tex(r"7 \mod 7 \equiv 0 \text{, so start there ...}").next_to(imagine, BOTTOM, buff=0.05)
        imagine_mod_2 = Tex(r"\text{... and `turn around' at 11, the end of the `window' ...}").next_to(imagine_mod, BOTTOM, buff=0.05)

        self.play(Write(imagine))
        self.play(Write(imagine_mod))
        self.play(Write(imagine_mod_2))

        still_2 = Tex(r"\text{In a different window}").to_edge(BOTTOM, buff=0.05)
        still = Tex(r"\text{We're still travelling from } 7 \mod 7 \equiv 0 \text{ to } 14 \mod 7 \equiv 0").next_to(still_2, TOP, buff=0.05)

        self.play(Write(still))
        self.play(Write(still_2))

        # Step 3: Slide window right by +5 -> [5, 12)
        new_bracket = Brace(number_line).scale(0.39).move_to(number_line.number_to_point((5+12)/2) + LEFT*0.2 + DOWN*0.6)
        new_label = new_bracket.get_tex(r"5 \leq x < 12")

        self.play(
            Transform(window_bracket, new_bracket),
            Transform(window_label, new_label)
        )

        # Move dot within new window to show same wrap-around
        moving_dot.move_to(number_line.number_to_point(7))
        self.play(FadeIn(moving_dot))

        dot_positions_shifted = [8, 9, 10, 11, 5, 6, 7] # Wrap at 12 -> 5
        for val in dot_positions_shifted:
            self.play(ApplyMethod(moving_dot.move_to, number_line.number_to_point(val)), run_time=0.5)
        for val in dot_positions_shifted:
            self.play(ApplyMethod(moving_dot.move_to, number_line.number_to_point(val)), run_time=0.5)

        # Fade out everything
        self.play(FadeOut(imagine), run_time=0.2)
        self.play(FadeOut(imagine_mod), run_time=0.2)
        self.play(FadeOut(imagine_mod_2), run_time=0.2)
        self.play(FadeOut(still), run_time=0.2)
        self.play(FadeOut(still_2), run_time=0.2)
        for arrow in arrows:
            self.play(FadeOut(arrow), run_time=0.2)
        
        self.play(FadeOut(VGroup(window_bracket, window_label, number_line, moving_dot)))

        # Step 4: Cartesian plane version
        grid = NumberPlane(x_range=(-9, 9, 1), y_range=(-9, 9, 1)).scale(0.3)
        self.play(ShowCreation(grid), run_time=2.0)

        main_line = Line(
            start=grid.c2p(-9, -7),
            end=grid.c2p(7, 9),
            color=TEAL,
            stroke_width=2
        ).set_opacity(0.5)
        self.play(ShowCreation(main_line), run_time=2.0)

        graph_line_text = new_bracket.get_tex(r"\text{line: } y = x + 2").next_to(grid)
        self.play(Write(graph_line_text))

        # Initial window: 0 <= x, y < 4
        origin = grid.coords_to_point(0, 0)
        top_left = grid.coords_to_point(0, 7)
        bottom_right = grid.coords_to_point(7, 0)

        sqr_width = np.linalg.norm(origin - top_left)  # Get width
        sqr_height = np.linalg.norm(origin - bottom_right) # Get height

        square_mid_2 = grid.coords_to_point(3.5, 3.5)
        square = Rectangle(width=sqr_width, height=sqr_height, color=BLUE).move_to(np.array([sqr_width/2, sqr_height/2, 0]))
        square_label = Tex(r"0 \leq (x, y) < 7", color=BLUE).next_to(square, UP)
        self.play(ShowCreation(square), Write(square_label))


        window_1_line_1 = Line(
            start=grid.c2p(0, 2),
            end=grid.c2p(5, 7),
            color=TEAL,
            stroke_width=10
        ).set_opacity(0.5)
        self.play(ShowCreation(window_1_line_1), run_time=1.0)

        window_1_line_2 = Line(
            start=grid.c2p(5, 0),
            end=grid.c2p(7, 2),
            color=TEAL,
            stroke_width=10
        ).set_opacity(0.5)
        self.play(ShowCreation(window_1_line_2), run_time=1.0)



        # Move point inside and wrap
        dot2d = Dot().move_to(grid.coords_to_point(0, 2)).set_color(YELLOW)
        self.play(FadeIn(dot2d))

        for x in range(18):
            dx, dy = (1, 1)
            if dot2d.get_center()[0] > grid.coords_to_point(6.5, 0)[0]:
                dx = -7  # Wrap around
                dy = 0
            if dot2d.get_center()[1] > grid.coords_to_point(0, 6.5)[1]:
                dx = 0
                dy = -7  # Wrap around
            new_pos = dot2d.get_center() + np.array([dx, dy, 0]) * grid.get_x_unit_size()
            self.play(ApplyMethod(dot2d.move_to, new_pos, run_time=0.5))

        self.play(FadeOut(window_1_line_1), run_time=0.2)
        self.play(FadeOut(window_1_line_2), run_time=0.2)

        # Move window elsewhere
        square_mid_2 = grid.coords_to_point(-5.5, -5.5)
        new_square = square.copy().move_to(np.array(square_mid_2))
        new_label = Tex(r"-9 \leq x,y < -2", color=BLUE).next_to(new_square, UP)
        self.play(Transform(square, new_square), Transform(square_label, new_label))



        window_2_line_1 = Line(
            start=grid.c2p(-9, -7),
            end=grid.c2p(-4, -2),
            color=TEAL,
            stroke_width=10
        ).set_opacity(0.5)
        self.play(ShowCreation(window_2_line_1), run_time=1.0)

        window_2_line_2 = Line(
            start=grid.c2p(-4, -9),
            end=grid.c2p(-2, -7),
            color=TEAL,
            stroke_width=10
        ).set_opacity(0.5)
        self.play(ShowCreation(window_2_line_2), run_time=1.0)



        # Repeat wrap motion
        dot2d.move_to(grid.coords_to_point(-7, -5))
        
        for x in range(18):
            dx, dy = (1, 1)
            if dot2d.get_center()[0] > grid.coords_to_point(-2.5, -0.5)[0]:
                dx = -7  # Wrap around
                dy = 0
            if dot2d.get_center()[1] > grid.coords_to_point(-4.5, -2.5)[1]:
                dx = 0
                dy = -7  # Wrap around
            new_pos = dot2d.get_center() + np.array([dx, dy, 0]) * grid.get_x_unit_size()
            self.play(ApplyMethod(dot2d.move_to, new_pos, run_time=0.5))

        self.wait(20)

