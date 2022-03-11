from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from sqlite3 import*

class connectorDB:
    def __init__(self,root):
        self.root = root
        titlespace = ' '
        self.root.title(102* titlespace + "MySQL Connector")
        self.root.geometry('800x700')
        self.root.resizable(width = False , height= False)
        mainframe = Frame(self.root , bd=10 ,width= 900,height=700 ,relief= RIDGE, bg=  "cadet blue")
        mainframe.grid()
        
        titleframe = Frame(mainframe, bd=7 ,width=770 , height=100 ,relief=RIDGE)
        titleframe.grid(row=1 ,column= 0)
        
        topframe = Frame(mainframe, bd=5 ,width=770 , height=500 ,relief=RIDGE)
        topframe.grid(row=1 ,column= 0)
        
        leftframe = Frame(topframe,bd=5,width=770,height=400 , padx=2 ,bg="cadet blue",relief= RIDGE)
        leftframe.pack(side=LEFT)
        leftframe1 = Frame(leftframe , bd=5 ,width=600 , height=180 , padx=2 ,pady=4, relief= RIDGE)
        leftframe1.pack(side=TOP ,padx=0 ,pady=0)


        rightframe = Frame(topframe,bd=5,width=100,height=400 , padx=2 ,bg="cadet blue" ,relief= RIDGE)
        rightframe.pack(side=RIGHT)
        rightframe1 = Frame(rightframe,bd=5,width=90,height=300 , padx=2 ,pady=2 ,relief= RIDGE)
        rightframe1.pack(side=TOP)
        #=====================================================================================================
        studentID = IntVar()
        firstname  = StringVar()
        surname = StringVar()
        address = StringVar()
        gender1 = StringVar()
        mobile = IntVar()
        #=======================================================================================================
        def iexit():
            iexit = tkinter.messagebox.askyesno("My conntion","Confirm if you want to exit")
            if iexit > 0:
                root.destroy()
                return 


        def reset():
            self.libltitle11.delete(0,END)
            self.libltitle22.delete(0,END)
            self.libltitle33.delete(0,END)
            self.libltitle44.delete(0,END)
            gender1.set(" ") 
            self.libltitle66.delete(0,END)
        def adddata():
            if studentID.get() == "" or firstname.get() == "" or surname.get() == "":
                tkinter.messagebox.showerror("My conntion","Enter coreect details")
            else:
                conn = connect('test.db')
               
                cn = conn.cursor()
                cn.execute("insert into mainss1 values (?,?,?,?,?,?)",( 
                studentID.get(),
                firstname.get(), 
                surname.get(),
                address.get(), 
                gender1.get(),
                mobile.get()
                ))
                conn.commit()
                conn.close()
                tkinter.messagebox.showinfo("My conntion","Record Enter Successfully")
        def displaydata():
            conn = connect('test.db')
            cn = conn.cursor()
            cn.execute("SELECT * from mainss1")
            result = cn.fetchall()
            if len (result) != 0 :
                self.student_recoeds.delete(*self.student_recoeds.get_children())
                for row in result:
                    self.student_recoeds.insert("",END,values=row)

            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("My conntion","display data Successfully")
        def traineeinfo (ev):
            viewinfo = self.student_recoeds.focus()
            lernerdata = self.student_recoeds.item(viewinfo)
            row = lernerdata["values"]
            studentID.set(row[0])
            firstname.set(row[1]) 
            surname.set(row[2])
            address.set(row[3])
            gender1.set(row[4])           
            mobile.set(row[5])
        def update():
            conn = connect('test.db')
               
            cn = conn.cursor()
            cn.execute("UPDATE  mainss1 set firstname = ?,surname =?,address =?,gender1 = ?,mobile =?  where studentID=?",( 
            
            firstname.get(), 
            surname.get(),
            address.get(), 
            gender1.get(),
            mobile.get(),
            studentID.get()
            ))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("My conntion","update  Successfully")
        def delete():
            conn = connect('test.db')
               
            cn = conn.cursor()
            cn.execute("delete from mainss1 where studentID=?",(studentID.get(),))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("My conntion","delete  Successfully")
            reset()
        def search():
            try:
                conn = connect('test.db')
                cn = conn.cursor()
                cn.execute("select * from mainss1 where studentID=?",(studentID.get(),))
                row = cn.fetchone()

                studentID.set(row[0])
                firstname.set(row[1]) 
                surname.set(row[2])
                address.set(row[3])
                gender1.set(row[4])           
                mobile.set(row[5])
                conn.commit()
            except:
                tkinter.messagebox.showinfo("My conntion","delete  Successfully")
                reset()

            conn.close()        
            

        #=====================================================================================================
        self.libltitle = Label(titleframe, font=("arial",40,'bold'), text="mysql connection")
        self.libltitle.pack()

        self.libltitle1 = Label(leftframe1, font=("arial",12,'bold'), text="student ID", bd=7)
        self.libltitle1.grid(row=0 ,column=0, sticky=W ,padx=5)
        self.libltitle11 = Entry(leftframe1, font=("arial",12,'bold'),  bd=5 , width=44, justify="left" ,textvariable= studentID)
        self.libltitle11.grid(row=0 ,column=1, sticky=W ,padx=5)

        self.libltitle2 = Label(leftframe1, font=("arial",12,'bold'), text="first name", bd=7,)
        self.libltitle2.grid(row=1 ,column=0, sticky=W ,padx=5)
        self.libltitle22 = Entry(leftframe1, font=("arial",12,'bold'),  bd=5 , width=44, justify="left",textvariable=firstname)
        self.libltitle22.grid(row=1 ,column=1, sticky=W ,padx=5)

        self.libltitle3 = Label(leftframe1, font=("arial",12,'bold'), text="surname", bd=7)
        self.libltitle3.grid(row=2 ,column=0, sticky=W ,padx=5)
        self.libltitle33 = Entry(leftframe1, font=("arial",12,'bold'),  bd=5 , width=44, justify="left",textvariable=surname)
        self.libltitle33.grid(row=2 ,column=1, sticky=W ,padx=5)

        self.libltitle4 = Label(leftframe1, font=("arial",12,'bold'), text="Address", bd=7)
        self.libltitle4.grid(row=3 ,column=0, sticky=W ,padx=5)
        self.libltitle44 = Entry(leftframe1, font=("arial",12,'bold'),  bd=5 , width=44, justify="left",textvariable=address)
        self.libltitle44.grid(row=3 ,column=1, sticky=W ,padx=5)

        self.libltitle5 = Label(leftframe1, font=("arial",12,'bold'), text="Gender", bd=7)
        self.libltitle5.grid(row=4,column=0, sticky=W ,padx=5)
        self.libltitle55 = ttk.Combobox(leftframe1, font=("arial",12,'bold') , width=42, state="readonly" ,textvariable=gender1)
        self.libltitle55["values"]=(" ","Female", "Male")
        self.libltitle55.current(0)
        self.libltitle55.grid(row=4 ,column=1)

        self.libltitle6 = Label(leftframe1, font=("arial",12,'bold'), text="Mobile", bd=7)
        self.libltitle6.grid(row=5 ,column=0, sticky=W ,padx=5)
        self.libltitle66 = Entry(leftframe1, font=("arial",12,'bold'),  bd=5 , width=44, justify="left",textvariable=mobile)
        self.libltitle66.grid(row=5 ,column=1, sticky=W ,padx=5)
        #==============================================================================================
        scroll_y = Scrollbar(leftframe, orient= VERTICAL)
        self.student_recoeds = ttk.Treeview(leftframe, height=14 ,columns=("stdid","firstname","surname","address","geneder","mobile")
        , yscrollcommand = scroll_y.set)
        scroll_y.pack(side=RIGHT , fill=Y  )
        self.student_recoeds.heading("stdid", text="student ID")
        self.student_recoeds.heading("firstname", text="firstname")
        self.student_recoeds.heading("surname", text="surname")
        self.student_recoeds.heading("address", text="address")
        self.student_recoeds.heading("geneder", text="geneder")
        self.student_recoeds.heading("mobile", text="mobile")
        
        self.student_recoeds["show"]="headings"

        self.student_recoeds.column("stdid", width= 70 )
        self.student_recoeds.column("firstname", width= 100 )
        self.student_recoeds.column("surname", width= 100 )
        self.student_recoeds.column("address", width= 100 )
        self.student_recoeds.column("geneder", width= 70 )
        self.student_recoeds.column("mobile", width= 70 )

        self.student_recoeds.pack(fill= BOTH , expand=1)
        self.student_recoeds.bind("<ButtonRelease-1>",traineeinfo)
        #==================================================================================
        self.btnAddNew = Button(rightframe1,font=("arial",12,'bold'), text= "Add New" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=adddata)
        self.btnAddNew.grid(row=0,column=1,pady=1)
        self.btnAddNew2 = Button(rightframe1,font=("arial",12,'bold'), text= "Display" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=displaydata)
        self.btnAddNew2.grid(row=1,column=1,pady=1)
        self.btnAddNew3 = Button(rightframe1,font=("arial",12,'bold'), text= "Update" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=update)
        self.btnAddNew3.grid(row=2,column=1,pady=1)
        self.btnAddNew4 = Button(rightframe1,font=("arial",12,'bold'), text= "Delete" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=delete)
        self.btnAddNew4.grid(row=3,column=1,pady=1)
        self.btnAddNew5 = Button(rightframe1,font=("arial",12,'bold'), text= "Search" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=search)
        self.btnAddNew5.grid(row=4,column=1,pady=1)
        self.btnAddNew6 = Button(rightframe1,font=("arial",12,'bold'), text= "Reset" , bd=4 , padx=24,pady=1,width=8 ,height=2 ,command=reset)
        self.btnAddNew6.grid(row=5,column=1,pady=1)
        self.btnAddNew7 = Button(rightframe1,font=("arial",12,'bold'), text= "Exit" , bd=4 , padx=24,pady=1,width=8 ,height=2,command=iexit)
        self.btnAddNew7.grid(row=6,column=1,pady=1)



        











root = Tk()
application = connectorDB(root)
root.mainloop()
    








    



