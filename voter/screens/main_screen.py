from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

screen_str = """
<MainScreen>
    MDScreen:
        name: "MainScreen"

        Label:
            text: "Main Screen"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}


"""


class MainScreen(Screen):
    Builder.load_string(screen_str)


