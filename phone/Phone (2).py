import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
Window.size =(400,600) 
kv= Builder.load_file('phone3.kv')
class Fapp (App):
    def build (self):
        self.title = "Drag App[Rakwan]"
        f= FloatLayout ()
        S= Scatter()
        l= Label(text='RAKWAN-Ali',font_size=28)
        f.add_widget (S)
        S.add_widget (l)
        return f
      
        

Fapp ().run ()