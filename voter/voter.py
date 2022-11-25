import os
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from screens.load_screen import LoadScreen
from screens.main_screen import MainScreen
from screens.login_screen import LoginScreen


class Voter(MDApp, Screen):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        self.window_settings()
        screen_manager.add_widget(LoadScreen(name="LoadScreen"))
        screen_manager.add_widget(LoginScreen(name="LoginScreen"))
        screen_manager.add_widget(MainScreen(name="MainScreen"))

        return screen_manager

    def on_start(self):
        if self._check_keys():
            Clock.schedule_once(self.change_screen_to_login, 3)
        else:
            Clock.schedule_once(self.change_screen_to_register, 3)

    def change_screen_to_main(self, dt):
        screen_manager.current = "MainScreen"

    def change_screen_to_login(self, dt):
        screen_manager.current = "LoginScreen"

    def change_screen_to_register(self, dt):
        from screens.register_screen import RegisterScreen
        screen_manager.add_widget(RegisterScreen(name="RegisterScreen"))
        screen_manager.current = "RegisterScreen"

    def window_settings(self):
        self.title = "Açık Oylama Sistemi"
        Window.size = [300, 600]
        self.theme_cls.theme_style = "Dark"

    def _check_keys(self) -> bool:
        private_key = os.getcwd() + "/keys/private_key.aos"
        public_key = os.getcwd() + "/keys/public_key.aos"
        password = os.getcwd() + "/keys/password.aos"

        if os.path.exists(private_key) and os.path.exists(public_key) and os.path.exists(password):
            return True
        else:
            return False


if __name__ == "__main__":
    Voter().run()
