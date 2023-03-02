import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()
cur.execute("create table ineuron.fsds(studentid int, firstname varchar(50), lastname varchar(50), registrationdate Date, class varchar(20), course_name varchar(50) )")

