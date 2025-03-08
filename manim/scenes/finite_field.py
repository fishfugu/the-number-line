from manim import *
from manimlib import *
from manimlib import ShowCreation

class FiniteFieldExample(ThreeDScene):
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

