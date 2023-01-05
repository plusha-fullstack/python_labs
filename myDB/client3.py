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
mycursor.execute("update product set `name` = 'SCorsezeMu388' where `id` = 16;")
db.commit()
mycursor.execute("INSERT INTO `product` ( `name`, `price`, `weight`, `material`, "
                 "`dopINFO`, `id_classification`, `id_producer`) VALUES ('Питон 2',"
                 " '999', '0.666', 'ТЕСТ2', NULL, '2', '2')")
db.commit()
mycursor.execute("DELETE FROM product WHERE `id`='112'");
db.commit()
mycursor.execute("Select * from product WHERE price >499")
for x in mycursor:
    print(x)
db.close()
