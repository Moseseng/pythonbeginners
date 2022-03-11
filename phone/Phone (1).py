from kivy.app import App
from kivy.core.window import Window
Window.size = (400,600)

Window.clearcolor = (1,0.1,0,1)
        
                            

class Name (App) :
    def build(self):
        self.title = 'Moses'
      
    
    pass
Name ().run () 