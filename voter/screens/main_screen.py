import self
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import OneLineIconListItem, OneLineListItem, TwoLineListItem

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
                
            ScrollView:
                pos_hint:{'center_y': .44}
                MDList:
                    id: md_list_container
                    OneLineListItem:
                        text: "------- Adaylar -------"
                    TwoLineListItem:
                        id: "1"
                        text: "1"
                        secondary_text: "Kara Parti"
                        on_release: root._oy_ver(self, "1")
                    TwoLineListItem:
                        id: "2"
                        text: "2"
                        secondary_text: "Halki Soy Partisi"
                        on_release: root._oy_ver(self, "2")
                    TwoLineListItem:
                        id: "3"
                        text: "3"
                        secondary_text: "Halk Fakir Biz Zengin Parti"
                        on_release: root._oy_ver(self, "3")
                    TwoLineListItem:
                        id: "4"
                        text: "4"
                        secondary_text: "Politikacilar Kraldir Partisi"
                        on_release: root._oy_ver(self, "4")
                    OneLineListItem:
                        text: "###########################"
                    
                    
"""


class MainScreen(Screen):
    Builder.load_string(screen_str)

    def on_enter(self, *args):
        self.ids.label_oy_sayisi.text = self._get_oy_sayisi()

    def _get_oy_sayisi(self):
        # Bu veri municipality'den gelmeli
        oy_sayisi = 11
        return str(oy_sayisi)

    def _oy_ver(self, pressed, list_id):
        print(pressed.text, list_id)
        print("SC text :" + pressed.secondary_text,  "id :"+list_id)
        toast("Oy verildi")

    def on_pre_enter(self, *args):
        if self.manager.get_screen("LoginScreen").password_check():
            pass
        else:
            self.parent.current = "LoginScreen"
