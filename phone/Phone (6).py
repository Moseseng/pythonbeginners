import datetime
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.size = (400, 600) 
class MyLabel (Label):
    text= str(datetime.datetime.now())
    time = StringProperty('')
    def on_time(self):
        self.text = str(datetime.datetime.now())


runTouchApp(MyLabel())