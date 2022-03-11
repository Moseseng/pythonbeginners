class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)





Classy.addItem("tophat")
































"""from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import requests
root = Tk()
root.title("gui")
photo = PhotoImage(file = "nas.png")    
root.iconphoto(False, photo)



















root.mainloop()"""






"""def hhh():
    if v.get() == "f":
        c = Label(root,text="this f").pack()

v = StringVar()
d= OptionMenu(root, v , "f","g").pack()



bn = Button(root, text ="jj", command = hhh).pack()"""



"""
def sel():
    f = "value" + str(v.get())
    ne = Label(root, text= f).pack()

v = DoubleVar()

ver = Scale(root,variable = v ,from_=0 ,to =100).pack()

bb = Button(root, text="fF", command = sel).pack()
"""




"""
def pope():
    x=messagebox.askquestion("this my pope","hello wollde")
    Label(root, text=x).pack()
    if x =="yes":
        top = Toplevel()
        lbl = Label(top, text="hello world").pack()
Button(root,text = "pope",command = pope).pack()
"""

'''def pope():
    x=messagebox.askquestion("this my pope","hello wollde")
    Label(root, text=x).pack()

Button(root,text = "pope",command = pope).pack()'''














#root.filename = filedialog.askopenfilename(initialdir = r"C:\Users\مكتب المشكاة\Desktop\project of python\image",title = "Select aFile",filetypes = (("Text files","*.PNG*"),("all files", "*.*")))

#my = Label(root, text=root.filename).pack()
#myimage= ImageTk.PhotoImage(Image.open(root.filename))
#myi =L
#abel(image=myimage).pack()
























"""r= IntVar()
modes= [("dd","dd"),("ff","FF"),("CC","cc")]

pizza =StringVar()

pizza.set("dd")
                                 
for x,y in modes:
    Radiobutton(root,text=x,variable=pizza,value=y).pack()




                                 
def hhh(value):
    my =Label(root,text=value)
    my.pack()

my= Label(root, text=pizza)

my.pack()
bbb = Button(root, text= "mylll",command=lambda: hhh(pizza.get()))
bbb.pack()

Radiobutton(root,text="opetion1",variable=r,value=1,command=lambda: hhh(r.get())).pack()
Radiobutton(root,text="opetion2",variable=r,value=2,command=lambda: hhh(r.get())).pack()"""


#frame= LabelFrame(root, text="this my frame ",padx=5,pady=5)
#frame.pack(padx=100,pady=100)
#b=Button(frame,text="dhgdujhsusuwsjs")
#b.pack()
