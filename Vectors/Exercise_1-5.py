'''
Exercise 1-5
Create a simulation of a car (or runner) that accelerates when you press the
up key and brakes when you press the down key.
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
        self.vel += self.acc
        self.vel.limit(100)
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

    def __init__(self, **kwargs):
        super(Highway, self).__init__(**kwargs)
        Window.bind(on_key_down=self._keydown)

    def update(self, dt):
        self.car.checkEdge()
        self.car.move()

    def _keydown(self, instance, key, *args):
        '''Keycode ref
        https://github.com/kivy/kivy/blob/master/kivy/core/window/__init__.py
        '''
        # Key Up
        if key == 273:
            self.car.acc -= PVector(.01,0)
            print("Vel", self.car.vel, "Acc", self.car.acc)
        # Key Down
        if key == 274:
            self.car.acc += PVector(.01,0)
            print("Vel", self.car.vel, "Acc", self.car.acc)


class Exercise_1_5_App(App):

    def build(self):
        h = Highway()
        Clock.schedule_interval(h.update, .01)
        return h


if __name__ == "__main__":
    Exercise_1_5_App().run()
