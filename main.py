from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from connected import Connected

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):

        sm = ScreenManager()
        sm.add_widget(Login(name="login"))
        sm.add_widget(Connected(name="connected"))

        return sm

if __name__ == '__main__':
    LoginApp().run()
