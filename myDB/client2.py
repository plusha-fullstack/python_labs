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
db.close()
