from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class whogoesfirst(GridLayout):
    def whogoesfirst(self):
        Player_Start = Button(text='I Start')
        Computer_Start = Button(text='You Start')
        content = BoxLayout(orientation='vertical')
        content.add_widget(Computer_Start)
        content.add_widget(Player_Start)

        popup = Popup(title='Who Goes First?',
                      content=content,
                      size_hint=(.8, .8)).open()

        Player_Start.bind(on_release=popup.dismiss)
        Computer_Start.bind(on_release=popup.dismiss)

        Player_Start.bind(on_release=self.placeX)
        Computer_Start.bind(on_release=self.AI)

    whogoesfirst()