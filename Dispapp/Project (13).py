import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
"""sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)"""
print("Table created successfully........")
cursor.execute('''SELECT * from EMPLOYEE''')

#Fetching 1st row from the table
result = cursor.fetchone();
#for i in result:
    #print(i)

#Fetching 1st row from the table
result = cursor.fetchall();
#print(result)
for i in result:
    for b in i:
        print(b)


# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
