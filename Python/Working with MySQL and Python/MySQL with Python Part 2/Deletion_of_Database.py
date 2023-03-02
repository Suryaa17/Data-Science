import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()

# To drop a database

cur.execute("drop database ineuron")

mydb.commit()