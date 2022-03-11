from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import cv2
from PIL import Image, ImageTk
import time
from sqlite3 import * 
import tkinter.messagebox

class tickets:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x500+1+1")
        self.root.title("Hospital management")
        self.root.configure(background = "silver")
        self.root.resizable(False,False)
        title = Label(self.root,text ="Hospital Management",bg="#33EBFF",font=("monospace",14,'bold'),fg='blue')
        title.pack()
        #manageb = Frame(self.root,bg='#F3F3F3')
        #manageb.place(x=1100,y=30,width=250,height=400)
        title = Label(self.root,text ="The tickets",bg="#33EBFF",font=("monospace",14,'bold'),fg='blue')
        title.place(x=600,y=30,width=140)
        #iamge1 = Label(self.root,text='add a picture',bg="#33EBFF",font=("monospace",14,'bold'),fg='blue')
        #iamge1.place(x=700,y=85,width=140,height=25)
        name0 = Label(self.root,text="Employee Name",bg="#33EBFF",font=("monospace",12,'bold'),fg='blue')
        name0.place(x=0,y=60,width=160)
        vlist = ["employee1","employee2","employee3"]
        empmame = ttk.Combobox(self.root, values = vlist)
        empmame.set("Pick an Option")
        empmame.place(x=170,y=60,width=160)
        name1 = Label(self.root,text="IDpatient",bg="#33EBFF",font=("monospace",12,'bold'),fg='blue')
        name1.place(x=0,y=90,width=160)
        name2 = Label(self.root,text="name's patient*",bg="#33EBFF",font=("monospace",10,'bold'),fg='blue')
        name2.place(x=0,y=130,width=160)
        name3 = Label(self.root,text="Patient attendant's name*",bg="#33EBFF",font=("monospace",10,'bold'),fg='blue')
        name3.place(x=0,y=170,width=160)
        name4 = Label(self.root,text="Telephone number",bg="#33EBFF",font=("monospace",10,'bold'),fg='blue')
        name4.place(x=0,y=210,width=160)
        name5 = Label(self.root,text="Patient attendant phone number",bg="#33EBFF",font=("monospace",8,'bold'),fg='blue')
        name5.place(x=0,y=250,width=160)
        name6 = Label(self.root,text="Gender",bg="#33EBFF",font=("monospace",8,'bold'),fg='blue')
        name6.place(x=0,y=330,width=160)
        vlist1= ["Male","female"]
        Combo1 = ttk.Combobox(self.root, values =vlist1 )
        Combo1.set("female or male")
        Combo1.place(x=170,y=330,width=160)
        name7 = Label(self.root,text="Ticket price",bg="#33EBFF",font=("monospace",8,'bold'),fg='blue')
        name7.place(x=0,y=370,width=160)
        vlist2 = ["No-Free","Student","Retired"]
        Combo2 = ttk.Combobox(self.root, values = vlist2)
        Combo2.set("Ticket price")
        Combo2.place(x=170,y=370,width=160)
        name7 = Label(self.root,text="The visit",bg="#33EBFF",font=("monospace",8,'bold'),fg='blue')
        name7.place(x=0,y=410,width=160)
        Combo2=Entry(self.root, font = ('calibre',10,'normal'))
        Combo2.place(x=170,y=410,width=160)
        enter1=Entry(self.root, font = ('calibre',10,'normal'))
        enter1.place(x=170,y=90,width=200,height=25)
        enter2=Entry(self.root, font = ('calibre',10,'normal'))
        enter2.place(x=170,y=130,width=200,height=25)
        enter3=Entry(self.root, font = ('calibre',10,'normal'))
        enter3.place(x=170,y=170,width=200,height=25)
        enter4=Entry(self.root, font = ('calibre',10,'normal'))
        enter4.place(x=170,y=210,width=200,height=25)
        enter5=Entry(self.root, font = ('calibre',10,'normal'))
        enter5.place(x=170,y=250,width=200,height=25)
        btn1 = Button(self.root, text = 'save', bd = '5',)
        btn1.place(x=150,y=440,width=100,height=25)
        btn2 = Button(self.root, text = 'Update', bd = '5',)
        btn2.place(x=250,y=440,width=100,height=25)
        btn3 = Button(self.root, text = 'research', bd = '5',)
        btn3.place(x=350,y=440,width=100,height=25)
        btn4 = Button(self.root, text = 'Print', bd = '5',)
        btn4.place(x=450,y=440,width=100,height=25)
        button1 = Button(self.root,text ='take photo',command = App, height=10, width=10)
        button1.place(x=550,y=440,width=100,height=25)
        button2 = Button(self.root,text ='show photo',command = myvideocapture.button1, height=2, width=10)
        button2.place(x=650,y=440,width=100,height=25)
        cal = Calendar(root, selectmode = 'day',year = 2020, month = 5,day = 22)
        cal.place(x=380 , y=90)
 
        def grad_date():
            date.config(text = "Selected Date is: " + cal.get_date())
 

        Button(root, text = "Get Date",command = grad_date).place(x=0,y=290)
 
        date = Label(root, text = "")
        date.place(x=170,y=290)
class App:
    def __init__ (self , video_source =0):
        self.appName ="CID Camera v1.0"
        self.window =Toplevel()
        self.window.title(self.appName)
        self.window.resizable(0,0)
        #self.window.wm_iconbitmap("cam.ico")
        self.window["bg"]= "black"
        self.video_source = video_source
        self.vid = myvideocapture(self.video_source)
        self.label = Label(self.window , text = self.appName ,font = 15, bg= "blue" ,fg='white')
        self.label.pack(side = TOP , fill = BOTH)
        self.canvas = Canvas(self.window , width = self.vid.width , height= self.vid.height,bg="red")
        self.canvas.pack()
        self.btn_snapshot = Button(self.window ,text = "SnapShot" , width =30 , bg ="goldenrod2" , activebackground = "red" , command = self.snapshot )
        self.btn_snapshot.pack(anchor = CENTER , expand = True )
        self.update()
        #self.window.mainloop()

    def snapshot(self):
        check , frame = self.vid.getframe()
        if check:
            image = "frame.png"
            cv2.imwrite(image, cv2.cvtColor(frame , cv2.COLOR_BGR2RGB))
            msg = Label (self.window , text ="image saved" + image , bg= "black", fg="green")
            msg.place(x= 430 , y= 510)
    def update (self):
        isTrue , frame = self.vid.getframe()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0,0, image = self.photo , anchor = NW)

        self.window.after(15, self.update)
                
#==========================================================
class myvideocapture :
    def __init__ (self , video_source =0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError ("unable to open this camera " ,video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def getframe(self):
        if self.vid.isOpened():
            isTrue , frame = self.vid.read()
            if isTrue:
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else :
                return (isTrue , None)
        else:
            return(isTrue , None)
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
    def button1():
        novi = Toplevel()
        canvas = Canvas(novi, width = 650, height = 500)
        canvas.pack(expand = YES, fill = BOTH)
        gif1 = PhotoImage(file = 'frame.png')
                                    #image not visual
        canvas.create_image(50, 10, image = gif1, anchor = NW)
        #assigned the gif1 to the canvas object
        canvas.gif1 = gif1
        

root = Tk()
tickets(root)
root.mainloop()
