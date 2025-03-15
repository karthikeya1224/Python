import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karthik@1224",
    database="mypythondb"
)
mycursor = mydb.cursor()
while True:
    name=input("enter name:").strip().lower()
    email=input("enter email:").strip().lower()
    sql = "INSERT INTO pythondb (name, email) VALUES (%s, %s)"
    value = (name,email)
    mycursor.execute(sql, value)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    ch=input("do you want to continue y/n")
    if ch=='n':
        break
