'''
Exercise 1-8
Try implementing the above example with a variable magnitude of acceleration,
stronger when it is either closer or farther away.
'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import ObjectProperty


class PVector(Vector):

    def __init__(self, *args, **kwargs):
        super(PVector, self).__init__(*args, **kwargs)

    def limit(self, val):
        if self.length() > val:
            #TODO: Limited value tends to drift over time
            #Possible solution: Decimal module
            self[0], self[1] = self.normalize() * val


class Car(Widget):

    vel = PVector(2, 0)
    acc = PVector(0, 0)

    def move(self):
        # Calculate the direction from mouse to ball
        dir = PVector(Window.mouse_pos) - self.pos
        # Acceleration gets stronger when it's close
        self.acc = dir.normalize() / dir.length() * 2

        self.vel += self.acc
        self.vel.limit(10)
        self.pos = PVector(self.pos) + self.vel

    def checkEdge(self):
        # check horizontal border
        if self.x > Window.width:
            self.x = 0
        elif self.x < 0:
            self.x = Window.width

        # check vertical border
        if self.y > Window.height:
            self.y = 0
        elif self.y < 0:
            self.y = Window.height


class Highway(Widget):

    car = ObjectProperty()

    def update(self, dt):
        self.car.checkEdge()
        self.car.move()


class Exercise_1_8_App(App):

    def build(self):
        h = Highway()
        Clock.schedule_interval(h.update, .01)
        return h


if __name__ == "__main__":
    Exercise_1_8_App().run()
