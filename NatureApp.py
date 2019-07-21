from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class SimuWindow(BoxLayout):
    pass

class NatrureApp(App):
    def build(self):
        return SimuWindow()

if __name__ == "__main__":
    NatrureApp().run()
