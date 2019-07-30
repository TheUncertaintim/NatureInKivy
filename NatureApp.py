from kivy.app import App
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from random import randint, choice, random
import numpy as np


class Walker(FloatLayout):

    points = ListProperty([])

    def __init__(self, **kwargs):
        super(Walker, self).__init__(**kwargs)

        # start random walk from the center
        self.points = Window.center
        # start walking
        Clock.schedule_interval(self.update, 0.1)

    def update(self, *args):

        # Get current position
        last_x = self.points[-2]
        last_y = self.points[-1]

        # 1.1 # Generate random steps in 9 possible directions
        new_x = randint(-1,1)
        new_y = randint(-1,1)

        # 1.2 # Or with a tendency moving down and right
        #new_x = choice([-1]*2 + [0]*2 + [1]*6)
        #new_y = choice([-1]*6 + [0]*2 + [1]*2)

        # 1.3 # 50% chance moving to where the mouse is
        #if random() <= 0.5:
        #    new_x = np.sign(Window.mouse_pos[0] - last_x)
        #    new_y = np.sign(Window.mouse_pos[1] - last_y)
        #else:
        #    new_x = randint(-1,1)
        #    new_y = randint(-1,1)

        # Add the next step based on the previous position
        self.points = self.points + [last_x + new_x, last_y + new_y]

class NatureApp(App):

    def build(self):

        return Walker()


if __name__ == "__main__":
    NatureApp().run()
