from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen


Window.clearcolor=(100/255.0,0,1,1) # red | green blue a 0=>255
Window.size=(370,630)

class MainWindow (Screen):
    pass 
class SecondScreen (Screen):
    pass
class Error1 (Screen):
    pass
class Python6 (Screen):
    pass
class Python5 (Screen):
    pass
class Python4 (Screen):
    pass
class Python3 (Screen):
    pass
class Python2 (Screen):
    pass
class Python1 (Screen):
    pass
class WindowManager (ScreenManager):
    pass
kv= Builder.load_file('my.kv')

class MyMainApp (App):
   def build (self):
        self.title='Rakwan Apps'
        return kv

MyMainApp ().run()