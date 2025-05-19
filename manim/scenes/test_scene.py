from manimlib import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, ManimGL!").scale(0.75)
        self.play(Write(text))
        self.wait()