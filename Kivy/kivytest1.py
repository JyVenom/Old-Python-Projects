import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):

    def build(self):
        return Label(text="Hello Kivy")

helloKivy = HelloKivy()

helloKivy.run()