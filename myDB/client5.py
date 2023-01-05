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
input_str = input("Enter your sql query: ")
cursor = db.cursor()
try:
    cursor.execute(input_str)
    for x in cursor:
        print(x)
    db.commit()
    print("Query executed successfully")
except:
    print("Query execution failed")
    exit(-2)
db.close()

