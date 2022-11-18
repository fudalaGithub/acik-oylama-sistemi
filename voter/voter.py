import os
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.textinput import TextInput
from screens.load_screen import LoadScreen
from screens.main_screen import MainScreen

class Voter(MDApp, Screen):
    global screen_manager
    screen_manager = ScreenManager()


    def build(self):
        self.settings()
        screen_manager.add_widget(LoadScreen(name = "LoadScreen"))
        screen_manager.add_widget(MainScreen(name = "MainScreen"))

        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen_to_main, 3)

    def change_screen_to_main(self, dt):
        screen_manager.current = "MainScreen"

    def settings(self):
        self.title = "Açık Oylama Sistemi"
        Window.size = [300, 600]
        self.theme_cls.theme_style = "Dark"




if __name__ == "__main__":
    Voter().run()
