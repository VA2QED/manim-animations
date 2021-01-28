from manim import *

# manimce v0.2.0
# background colour of #FFFFFF
"""
Text: We are in the midst of  pandemic. 
        Suffering from anxiety, depression or any type of
        mental illness is never a sign of weakness.

Text: There are plenty of resources that
        aim towards helping the community to 
        overcome mental illnesses.
Bell Let's talk logo join the conversation
Kids Help Phone contact information
"""


# chances are i won't get sued for doing this but i'm adding it just in case
class Unofficial(Scene):
    def construct(self):
        warning = Text("""
        This video was made
        in good faith to
        start the conversation
        on mental health. This video
        IS NOT affiliated with or
        endorsed by Bell Let's Talk.
        """)
        warning.set_color(BLACK)
        self.play(Write(warning))
        self.wait()


class BellLetsTalk(Scene):
    def construct(self):
        Text1 = Text("""
        We are in the midst of a 
        historic pandemic.
        Suffering from anxiety,
        depression or any type 
        of mental illness is 
        never a sign of weakness. 
                     """)

        Text2 = Text("""
        There are plenty of
        resources that aim towards 
        helping the community
        to overcome mental illness. 
        """)
        Text3 = Text("""
        But most importantly, 
        your friends, family 
        and community may be
        more supportive 
        than you can imagine.
        """)
        Text1.set_color_by_gradient('#005388', BLACK)  # the first colour is the colour of bell's logo
        Text2.set_color_by_gradient(BLACK, '#005388')  # change the order just for variety
        Text3.set_color_by_gradient('#005388', BLACK)  # also, the text colour is black because it will
                                                       # be rendered on a white background
        self.play(Write(Text1), run_time=4)
        self.wait(3)
        self.play(ReplacementTransform(Text1, Text2))
        self.wait(3)
        self.play(ReplacementTransform(Text2, Text3))
        self.wait(3)


class Resources(Scene):
    def construct(self):
        bell_logo = ImageMobject("./assets/bell_lets_talk/bell_lets_talk_logo.png")
        bell_logo.move_to(np.array([-4, 2, 0])).scale(0.4)

        end_stigma = Text("End the stigma\nof mental health.")
        end_stigma.set_color_by_gradient('#005388', BLACK)
        end_stigma.next_to(bell_logo)

        khp_logo = ImageMobject("./assets/bell_lets_talk/KHP.png")
        khp_logo.move_to(np.array([0, 0.5, 0]))

        khp_contact = Text("1-800-668-6868\nKidsHelpPhone.ca")
        khp_contact.next_to(khp_logo, direction=DOWN)
        khp_contact.set_color('#00a3d8')

        self.play(FadeInFrom(bell_logo, direction=DOWN))
        self.play(Write(end_stigma))
        self.wait()
        self.play(FadeInFrom(khp_logo, direction=LEFT))
        self.play(Write(khp_contact))
        self.wait(2)


# TODO: this is a bad way of concatenating the scenes because it doesn't actually instantiate each scene but
#  rather passes everything as a function. Any pull requests on this would be appreciated
class Everything(Scene):
    def construct(self):
        Unofficial.construct(self)
        self.clear()
        BellLetsTalk.construct(self)
        self.clear()
        Resources.construct(self)