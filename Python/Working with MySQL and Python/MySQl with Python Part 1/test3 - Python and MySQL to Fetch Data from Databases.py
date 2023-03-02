import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()
cur.execute("select * from suryaa.fsds")

for i in cur:
    print(i)