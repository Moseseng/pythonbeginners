
from tkinter import *

from tkinter import messagebox
import sqlite3

root=Tk()
root.title("codemy ")
root.geometry("500x500")
#root.resizable(False, False)


conn = sqlite3.connect('database.db')
# cursor to move in the database
c = conn.cursor()
"""(c.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   fname text,
   lname text,
   adname text,
   ciname text,
   stname text
   ziname text,
)'''
c.execute(sql))"""


def clearTextInput():
    dgh=[fname.get(),lname.get(),ci.get(),ad.get(),stname.get(),ziname.get()]
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO EMPLOYEE VALUES (?,?,?,?,?,?)''',dgh)
    conn.commit()
    conn.close()







    
    fname.delete(0,END)
    lname.delete(0,END)
    ci.delete(0,END)
    ad.delete(0,END)
    stname.delete(0,END)
    ziname.delete(0,END)
    fname.focus()


def clear():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM EMPLOYEE WHERE  ")
    c.fetchone()
    result=c.fetchall()
    print_i = ''
    for i in result:
        for b in i:
    
            print_i += str(b) +'\n'
            query_ = Label(root,text =print_i ).place(x=450, y=450)

    
    conn.commit()
    conn.close()    

frm= Frame(root, width=600, height=720, bg='lightblue').pack(side = LEFT)
right = Frame(root, width=400, height=720, bg='steelblue').pack(side = RIGHT)


heading = Label(root, text="Enter details", font=('arial 18'), fg='black', bg='lightblue').place(x=220, y=50)

        # patient's name
fname1 = Label(root, text="Patient's Name", font=('arial 12'), fg='black', bg='lightblue')
fname1.place(x=65, y=100)

        # age
lname1 = Label(root, text="lname", font=('arial 12'), fg='black', bg='lightblue')
lname1.place(x=65, y=140)

        # gender
ci1 = Label(root, text="ci", font=('arial 12'), fg='black', bg='lightblue').place(x=65, y=180)

        # location
ad1 = Label(root, text="ad", font=('arial 12'), fg='black', bg='lightblue').place(x=65, y=220)

        # appointment time
stname1 = Label(root, text="stname", font=('arial 12'), fg='black', bg='lightblue').place(x=65, y=260)

        # phone
ziname1 = Label(root, text="ziname", font=('arial 12'), fg='black', bg='lightblue').place(x=65, y=300)

       #
fname=Entry (root, width=30)
fname.place(x=275, y=100)

lname= Entry(root, width=30)
lname.place(x=275, y=140)


ci = Entry(root, width=30)
ci.place(x=275, y=220)

ad= Entry(root, width=30)
ad.place(x=275, y=260)

stname= Entry(root, width=30)
stname.place(x=275, y=300)
ziname =Entry(root, width=30)
ziname.place(x=275, y=180)

submit = Button(root, text="Add Appointment", width=20, height=2, bg='steelblue', command=clearTextInput).place(x=190, y=350)
QUREY = Button(root, text="show records", width=20, height=2, bg='steelblue', command=clear).place(x=220, y=400)
gg =Button(root, text="show records", width=20, height=2, bg='steelblue', command=clear).place(x=400, y=500)









conn.commit()
conn.close()
root.mainloop()













