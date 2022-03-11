from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties  import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.core.window import Window
Window.clearcolor = (100/255.0,0,0,0)
Builder.load_string('''
<Scroll>:
    text: 'gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'*100
    Label:
        text: root.text
        font_size: 44
        text_size: self.width,None
        size_hint_y: None
        height: self.texture_size[1] 

  ''')
class Scroll (ScrollView):
    text= StringProperty('')
runTouchApp (Scroll())