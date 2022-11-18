from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

screen_str = """
<LoadScreen>
    MDScreen:
        name: "LoadScreen"

        Label:
            text: "Acık Oylama Sistemine"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            
        Label:
            text: "Hoş Geldiniz"
            pos_hint:{'center_x': 0.5, 'center_y': 0.45}

"""


class LoadScreen(Screen):
    Builder.load_string(screen_str)

