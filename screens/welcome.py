from kivy.uix.screenmanager import Screen, SlideTransition
from kivyauth.utils import auto_login, login_providers
from kivyauth.google_auth import initialize_google


class Welcome(Screen):

    def on_start(self):
        if auto_login(login_providers.google):
            self.current_provider = login_providers.google

    def login(self):
        initialize_google(self.after_login, self.error_listener)

    def after_login(self, **qwargs):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'clients'

    def error_listener(self, **qwargs):
        pass
