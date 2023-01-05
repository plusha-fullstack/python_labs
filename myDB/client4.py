import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="mydb"

    )
    print("Connection successful")
except:
    print("Connection failed")
    exit(-1)
mycursor = db.cursor()
mycursor.execute("Select * from product WHERE price >499")
for x in mycursor:
    print(x)
db.close()

