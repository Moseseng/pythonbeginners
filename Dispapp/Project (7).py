from sqlite3 import *
f = connect("test.db")
b = f.cursor()

b.execute("CREATE TABLE IF NOT EXISTS Iamge (id INTEGER NOT NULL  PRIMARY KEY , PHOTO LONGBLOB NOT NULL)")

def insertblop(file):
    f = connect("test.db")
    b = f.cursor()
    with open (file , "rb") as fi:
        binary = fi.read()
    msqle = "INSERT INTO Iamge (Photo)VALUES (?)"
    b.execute(msqle ,(binary,))
    f.commit()
    f.close()

def readi(ID):
    f = connect("test.db")
    b = f.cursor()
    msql2 = "SELECT * FROM Iamge WHERE id = {0}"
    b.execute(msql2.format(str(ID)))
    myresult = b.fetchone()[1]
    storef = "format.png"
    print(myresult)
    with open(storef , "wb") as fg:
        fg.write(myresult)
    f.commit()
    f.close()
    



print("1.insert image \n2.read image")

me = input()
if int(me) == 1:
    userfile = input("enter file path :")
    insertblop(userfile)
elif int(me)== 2:
    userid = input("enter id")
    readi(userid)























