#! /usr/bin/env python

#using manimlib-0.1.11
from manimlib.imports import *
from math import *
# I don't think that this import is mandatory. Pycharm doesn't recognize the constants defined in the manim dictionaries
from pygments.styles.rainbow_dash import *

# TODO: Make methods of declaring configurations to be consistent. 
class OpeningScene(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -2,
        "y_max": 2,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "x_axis_label": "$\\theta$",
        "y_axis_label": "$f(\\theta)$"
    }

    def construct(self):
        self.setup_axes(animate=True)
        title = TexMobject(
            "\\text{Finding }\\lim_{\\theta \\to 0} \\frac{\\sin \\theta}{\\theta}") \
            .move_to(TOP - 1 + LEFT) \
            .set_color_by_gradient(GREEN, YELLOW)
        sinx_x_graph = self.get_graph(self.sinx_x_to_graph, WHITE)
        label = self.get_graph_label(sinx_x_graph, label="\\frac{\\sin \\theta}{\\theta}", color=PURPLE)
        undefined_point = Dot(self.coords_to_point(0, 1),
                              stroke_width=3.0,
                              fill_opacity=1.0,
                              fill_color=BLACK,
                              radius=0.08,
                              color=YELLOW
                              )

        self.play(Write(title))
        self.play(ShowCreation(sinx_x_graph), Write(label), ShowCreation(undefined_point))
        self.wait(5)

	# Here's something interesting: if you don't define x at 0 to be 1, manim will draw a spike at the point zero. Probably because python defines undefined values as a large number or something and manim smooths the graph out.
    def sinx_x_to_graph(self, x):
        if x == 0:
            return 1
        else:
            return sin(x) / x

# TODO: Wouldn't it be cool if we can animate the angle theta to get smaller and smaller?
class UnitCircle(GraphScene):
    CONFIG = {
        "x_min": -1.5,
        "x_axis_width": 6,
        "x_max": 1.5,
        "y_min": -1.5,
        "y_axis_height": 6,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.wait()

        # the y length is the radius of the circle, this should work fine.
        unit_circle = Circle(radius=self.coords_to_point(0 , 1)[1], color=WHITE)
        unit_circle_postulate = TextMobject("Postulate a unit circle\\\\ and the angle $\\theta$")\
            .move_to(3*UP+3*LEFT)

        hypotenuse = Line(self.coords_to_point(0,0), self.coords_to_point(sqrt(3)/2, 1/2))
        angle_arc = Arc(0, TAU/12, radius=0.5)
        angle_arc_theta = TextMobject("$\\theta$").move_to(
            np.array([angle_arc.get_x() + 0.35, angle_arc.get_y() + 0.1, 1])
        )

        self.play(ShowCreation(unit_circle), Write(unit_circle_postulate))
        self.play(ShowCreation(hypotenuse), ShowCreation(angle_arc), Write(angle_arc_theta))
        self.wait(3)

        sine_line = Line(
            self.coords_to_point(sqrt(3)/2,0), self.coords_to_point(sqrt(3)/2, 1/2),
            color=GREEN
        )
        sine_line_description = TextMobject(
            "This line has the \\\\ length of $\\sin \\theta$.",
            color=GREEN,
        ).move_to(3*UP+3*LEFT)

        self.play(ShowCreation(sine_line))
        self.play(ReplacementTransform(unit_circle_postulate, sine_line_description))
        self.wait(3)

        unit_circle_arc = Arc(0, TAU/12, radius=self.coords_to_point(0,1)[1]).set_color(YELLOW).set_depth(-10)
        unit_circle_arc_description = TextMobject("This arc has the \\\\ length of $\\theta$.")\
            .set_color(YELLOW)\
            .move_to(3*UP+3*LEFT)

        self.remove(sine_line_description)
        self.play(ShowCreation(unit_circle_arc),
                  ReplacementTransform(unit_circle_postulate, unit_circle_arc_description)
                  )
        self.wait(3)

        tangent_line = Line(
            self.coords_to_point(1,0), self.coords_to_point(1, sqrt(3)/3),
            color=RED
            )
        triangle_tangent_line_extension = Line(
            self.coords_to_point(sqrt(3)/2, 1/2), self.coords_to_point(1,sqrt(3)/3),
            color=GRAY
        )
        tangent_line_description = TextMobject("This line has the length \\\\ of $\\tan \\theta$",
                                               color=RED
                                               ).move_to(3*UP+3*LEFT)

        self.remove(unit_circle_arc_description)
        self.play(ShowCreation(tangent_line), ShowCreation(triangle_tangent_line_extension))
        self.play(Write(tangent_line_description))
        self.wait(4)

# TODO: Add colours to each term to make it easier to identify what it is representing on the unit circle, or better yet, combine this scene to the unit circle scene.
class Derivation(Scene):
    def construct(self):
        inequality_description = TextMobject("As $\\theta$ approaches 0, the following inequality holds true:")
        starting_expression = TexMobject("\\sin \\theta \\leq \\theta \\leq \\tan \\theta")
        expressions = [
            TexMobject("\\frac{1}{\\sin \\theta} \\geq \\frac{1}{\\theta} \\geq \\cot \\theta"),
            TexMobject("\\sin \\theta \\cdot \\frac{1}{\\sin \\theta} \\geq \\sin \\theta \\cdot \\frac{1}{\\theta} \\geq \\sin \\theta \\cdot  \\cot \\theta"),
            TexMobject("1 \\geq \\frac{\\sin \\theta}{\\theta}\\geq \\cos \\theta"),
            TexMobject("\\lim_{\\theta \\to 0} 1 \\geq \\lim_{\\theta \\to 0}\\frac{\\sin \\theta}{\\theta} \\geq \\lim_{\\theta \\to 0} \\cos \\theta"),
            TexMobject("1 \\geq \\lim_{\\theta \\to 0}\\frac{\\sin \\theta}{\\theta} \\geq 1"),
        ]
        squeeze_theorem = TexMobject("\\text{Therefore, by the squeeze theorem, }\\lim_{\\theta \\to 0} \\frac{\\sin \\theta}{\\theta}=1")
        self.play(Write(inequality_description))
        self.wait(5)
        self.play(VFadeOut(inequality_description))
        self.play(Write(starting_expression))
        self.wait(4)
        for expression in expressions:
            self.play(Transform(starting_expression, expression))
            self.wait(5)
        self.play(FadeOut(starting_expression))
        self.play(Write(squeeze_theorem))
        self.wait(3)


class FootNote(Scene):
    def construct(self):
        side_note = TextMobject("Side note, I technically only proved\\\\the limit approaching from the positive side.\\\\ For this limit to hold true, the one sided limit\\\\ from the negative side must also be 1\\\\ However, this is trivial and is left as an exercise to the viewer.\\\\ Kidding, I spent way too long on this animation\\\\ and you can find the full proof from BlackPenRedPen.")
        self.play(Write(side_note))
        self.wait(10)
