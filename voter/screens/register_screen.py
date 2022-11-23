from kivy.lang import Builder
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from cryptographerAos.cryptographerAos import CryptographerAos

screen_str = """
<RegisterScreen>
    MDScreen:
        name: "RegisterScreen"
        
        MDBoxLayout:
            orientation: "vertical"
            spacing: "20dp"
            adaptive_height: True
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}
            
            Label:
                id: label_up
                text: "Lütfen anahtar oluşturun"
        
            MDTextField:
                id: isim_text_field
                mode: "rectangle"
                hint_text: 'İsim'
                
            MDTextField:
                id: soyisim_text_field
                mode: "rectangle"
                hint_text: 'Soyİsim'
                
            MDTextField:
                id: sifre_text_field
                mode: "rectangle"
                hint_text: "Şifre"
                password: True
                
            MDTextField:
                id: tekrar_sifre_text_field
                mode: "rectangle"
                hint_text: "Tekrar Şifre"
                password: True
                
            MDRaisedButton:
                id: anahtar_olustur_btn
                text: "Anahtar Oluştur"
                pos_hint: {"center_x": 0.5}
                md_bg_color: "red"
                on_press: root._anahtar_olustur_btn()



"""


class RegisterScreen(Screen):
    Builder.load_string(screen_str)

    def _anahtar_olustur_btn(self):

        if self.__input_control():
            inputs_list = self.__get_inputs_in_list()
            del inputs_list[-1::]
            key_string = self.__convert_list_to_string(inputs_list)
            private_key = CryptographerAos().do_Hash256(key_string)
            public_key = CryptographerAos().do_Hash256(private_key)
            password = self.__convert_list_to_string(inputs_list[-1:])
            CryptographerAos().save_private_key(private_key)
            CryptographerAos().save_public_key(public_key)
            CryptographerAos().save_password(CryptographerAos().do_Hash256(password))  # Şifre doğrudan kaydedilmemeli
            toast('Anahtar Oluşturuldu')
            self.parent.current = "MainScreen"


    def __input_control(self) -> bool:

        input_list = self.__get_inputs_in_list()

        if not input_list[0]:
            toast('Lütfen isim giriniz')
        else:
            if not input_list[1]:
                toast('Lütfen soyisim giriniz')
            else:
                if not input_list[2]:
                    toast('Lütfen şifre giriniz')
                else:
                    if not input_list[3]:
                        toast('Lütfen tekrar şifre giriniz')
                    else:
                        if input_list[2] == input_list[3]:
                            return True
                        else:
                            toast("Şifreler eşleşmiyor, lütfen tekrar girin")

        return False

    def __get_inputs_in_list(self) -> list:
        inputs_list = []
        inputs_list.append(self.ids.isim_text_field.text)
        inputs_list.append(self.ids.soyisim_text_field.text)
        inputs_list.append(self.ids.sifre_text_field.text)
        inputs_list.append(self.ids.tekrar_sifre_text_field.text)

        return inputs_list

    def __convert_list_to_string(self, list) -> str:
        converted_list = ' '.join(list)
        return converted_list
