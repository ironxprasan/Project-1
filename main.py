from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class interface(FloatLayout):

    def DispayInterface(self):
        dta = self.ids.textinput.text
        self.ids.label.text = dta


class ProjectApp(App):

    pass


ProjectApp().run()
