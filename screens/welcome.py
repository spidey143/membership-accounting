from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition



class Welcome(Screen):

    def login(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'clients'
