from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

screen_str = """
<RegisterScreen>
    MDScreen:
        name: "RegisterScreen"

        Label:
            text: "Register Screen"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}


"""


class RegisterScreen(Screen):
    Builder.load_string(screen_str)


