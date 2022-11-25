import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from cryptographerAos.cryptographerAos import CryptographerAos

screen_str = """
<LoginScreen>
    MDScreen:
        name: "LoginScreen"

        MDBoxLayout:
            orientation: "vertical"
            spacing: "20dp"
            adaptive_height: True
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}
            
            Label:
                text: "Şifrenizi Girin"
        
            MDTextField:
                id: sifre_text_field
                mode: "rectangle"
                hint_text: "Şifre"
                password: True
                
                
            MDRaisedButton:
                id: giris_yap_btn
                text: "Giriş Yap"
                pos_hint: {"center_x": 0.5}
                md_bg_color: "red"
                on_press: root._giris_yap_btn()


"""


class LoginScreen(Screen):
    Builder.load_string(screen_str)

    def _giris_yap_btn(self):
        password_from_sifre_text_field = self.ids.sifre_text_field.text
        if not password_from_sifre_text_field:
            toast("Lütfen Şifrenizi girin")
        else:
            if self._password_check():
                toast("Giriş yapıldı")
                self.parent.current = "MainScreen"
            else:
                toast("Şifre Hatalı")

    def _password_check(self):
        password_from_sifre_text_field = self.ids.sifre_text_field.text
        password_from_file = self._get_password_key_from_file()

        try:
            hashed_password_from_sifre_text_field = CryptographerAos().do_Hash256(password_from_sifre_text_field)
            if password_from_file == hashed_password_from_sifre_text_field:
                return True
        except:
            print("_password_check Error: ")
            toast("_password_check Error: ")

        return False


    def _get_password_key_from_file(self):
        password_file = os.getcwd() + "/keys/password.aos"

        with open(password_file, "r", encoding="utf-8") as file:
            password_key = file.read()

            return password_key


