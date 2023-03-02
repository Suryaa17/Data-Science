import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()

# To fetch all data in the table

cur.execute("select * from ineuron.fsds")

for i in cur:
    print(i)

# To Fetch particular column from the database

cur.execute("select firstname,lastname,class from ineuron.fsds")

for i in cur:
    print(i)

# To fetch a particular data

cur.execute("select * from ineuron.fsds where studentid = 125")

for i in cur:
    print(i)

# To fetch particular set of data from the table

cur.execute("select * from ineuron.fsds where studentid > 128")

for i in cur:
    print(i)

# to fetch data with two or more parameters

cur.execute("select * from ineuron.fsds where studentid = 125 and class = 'sql'")

for i in cur:
    print(i)

# Updating data in database

cur.execute("update ineuron.fsds set firstname = 'suryaa' where studentid = 125")

mydb.commit()

# Updating entire column in a database

cur.execute("update ineuron.fsds set class = 'MySQl'")

mydb.commit()

# To Delete a row of data from the database

cur.execute("delete from ineuron.fsds where lastname = 'gupta'")

mydb.commit()

# To find minimum value in the database

cur.execute("select min(studentid) from ineuron.fsds")

for i in cur:
    print(i)

# To find maximum value in the database

cur.execute("select max(studentid) from ineuron.fsds")

for i in cur:
    print(i)

# To find the total number of records available in the database

cur.execute("select count(*) from ineuron.fsds")

for i in cur:
    print(i)

# To update Records

cur.execute("update ineuron.fsds set class = 'sql' where studentid between  125 and 128")

mydb.commit()

# To update records

cur.execute("update ineuron.fsds set class = 'mongoDB' where studentid between  129 and 133")

mydb.commit()

# To group the values in the column 

cur.execute("select count(*),class from ineuron.fsds group by class")

for i in cur:
    print(i)

# To drop or delete a table

cur.execute("drop table ineuron.fsds")

mydb.commit()


