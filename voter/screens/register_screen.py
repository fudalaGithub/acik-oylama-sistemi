from kivy.lang import Builder
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen

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
            print(".....")

        
        
    def __input_control(self) -> bool:  
        isim = self.ids.isim_text_field.text
        soyisim = self.ids.soyisim_text_field.text
        sifre = self.ids.sifre_text_field.text
        tekrar_sifre = self.ids.tekrar_sifre_text_field.text
        
        if not isim:
            toast('Lütfen isim giriniz')
        else:
            if not soyisim:
                toast('Lütfen soyisim giriniz')
            else:
                if not sifre:
                    toast('Lütfen şifre giriniz')
                else:
                    if not tekrar_sifre:
                        toast('Lütfen tekrar şifre giriniz')
                    else:
                        if sifre == tekrar_sifre:
                            return True
                        else:
                            toast("Şifreler eşleşmiyor")
                        
        return False




