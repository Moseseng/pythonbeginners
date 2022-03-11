import sqlite3
from openpyxl import Workbook 
wb = Workbook()  
sheet = wb.active 

conn = sqlite3.connect('test.db')
#print ("Opened database successfully")

#conn.execute('''CREATE TABLE mainss1
 #        (
  #       studentID           TEXT    NOT NULL,
   #      firstname           TEXT     NOT NULL,
    #     surname             TEXT NOT NULL ,
     #    address             TEXT NULL,
      #   gender1              TEXT NULL,
       #  mobile              INT NOT NULL );''')
#print ("Table created successfully")
cursor = conn.execute("SELECT * from mainss1")
for i in cursor:
    sheet.append(i)
wb.save('appending_values.xlsx')
 

conn.close()




















