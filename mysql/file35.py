import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="karthik@1224",
    database="learners"
)
mycursor=mydb.cursor()
mycursor.execute("select * from learners")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)