import self
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

screen_str = """
<MainScreen>
    MDScreen:
        name: "MainScreen"
        
        FloatLayout:
            Label:
                text: "Oy sayısı: "
                pos_hint:{'center_x': 0.14, 'center_y': .97}
            Label:
                id: label_oy_sayisi
                text: "0"
                pos_hint:{'center_x': 0.27, 'center_y': .97}
                
        RecycleBoxLayout:
            id: rv
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
"""


class MainScreen(Screen):
    Builder.load_string(screen_str)

    def on_enter(self, *args):
        pass

    def _get_oy_sayisi(self):
        pass
    def on_pre_enter(self, *args):
        if self.manager.get_screen("LoginScreen").password_check():
            pass
        else:
            self.parent.current = "LoginScreen"
