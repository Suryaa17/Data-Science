import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("create database suryaa")

# cur.execute("show databases")
# for i in cur:
#     print(i)

cur.execute("use suryaa")

# cur.execute("create table fsds(name varchar(10),rollno int,batch varchar(10))")

# cur.execute("select * from fsds")

cur.execute("insert into fsds values('suryaa',10,'september')")

mydb.commit()
