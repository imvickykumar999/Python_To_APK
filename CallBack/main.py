
import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.button import Button
from kivymd.uix.screen import Screen

import requests
from requests.structures import CaseInsensitiveDict

url = "https://neosalpha-999-default-rtdb.firebaseio.com/cURL/Switch.json"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

class ButtonApp(App):
    def build(self):
        screen = Screen()

        btn_ON = Button(text ="ON",
                font_size ="20sp",
                background_color =(1, 1, 1, 1),
                color =(1, 1, 1, 1),
                size_hint =(.2, .2),
                pos =(300, 200))

        btn_OFF = Button(text ="OFF",
                font_size ="20sp",
                background_color =(1, 1, 1, 1),
                color =(1, 1, 1, 1),
                size_hint =(.2, .2),
                pos =(300, 400))

        btn_ON.bind(on_press = self.callback_ON)
        btn_OFF.bind(on_press = self.callback_OFF)

        screen.add_widget(btn_OFF)
        screen.add_widget(btn_ON)
        return screen
        
    def callback_ON(self, event):
        requests.put(url, headers=headers, data="1")

    def callback_OFF(self, event):
        requests.put(url, headers=headers, data="0")

root = ButtonApp()
root.run()
