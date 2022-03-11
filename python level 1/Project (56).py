from ursina import *

def update():
    if held_keys['a']:
        teat_square.x -= 1 * time.dt
    
    elif held_keys['d']:
        teat_square.x += 1 * time.dt    


app = Ursina()
teat_square = Entity(model = "cube",color = color.red ,scale =(1,4),position = (5,1))

sans_texture = load_texture("assets\\Sans.png")

sans = Entity(model = "cube", texture = sans_texture )
app.run()

