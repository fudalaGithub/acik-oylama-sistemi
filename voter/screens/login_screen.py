from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

screen_str = """
<LoginScreen>
    MDScreen:
        name: "LoginScreen"

        Label:
            text: "Login Screen"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}


"""


class LoginScreen(Screen):
    Builder.load_string(screen_str)
    