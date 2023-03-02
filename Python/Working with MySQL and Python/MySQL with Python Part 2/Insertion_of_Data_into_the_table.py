import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

print(mydb.is_connected())

cur = mydb.cursor()

cur.execute("""insert into ineuron.fsds values(123 , 'sudhanshu', 'kumar','2022-11-11','sql','fsds'),
(124 , 'r', 'singh','2022-11-11','sql','fsds'),
(125 , 'rohan', 'kumar','2022-11-11','sql','fsds'),
(126 , 'shreeja', 'maynale','2022-11-11','sql','fsds'),
(127 , 'shubham', 'vedi','2022-11-11','sql','fsds'),
(128 , 'abhishek', 'saini','2022-11-11','sql','fsds'),
(129 , 'manoj', 'tripathi','2022-11-11','sql','fsds'),
(130 , 'mayur ', 'gupta','2022-11-11','sql','fsds'),
(131 , 'sumay', 'cahtterjee','2022-11-11','sql','fsds'),
(132 , 'raunak', 'shgaow','2022-11-11','sql','fsds'),
(133 , 'danish', 'khan','2022-11-11','sql','fsds')""")

mydb.commit()

cur.execute("select * from ineuron.fsds")

for i in cur:
    print(i)