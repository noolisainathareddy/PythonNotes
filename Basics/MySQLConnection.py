import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="1934Sai@", database="aetna")
except Exception as e:
    print(e)

if mydb.is_connected():
    print("Connection established")

mycursor = mydb.cursor()
mycursor.execute("select * from user_info")

for i in mycursor:
    print(i)
 
mycursor.close()

mydb.close()
