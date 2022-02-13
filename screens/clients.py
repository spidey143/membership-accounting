from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class Clients(Screen):

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'welcome'
