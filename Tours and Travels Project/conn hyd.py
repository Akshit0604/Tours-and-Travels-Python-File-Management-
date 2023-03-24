import mysql.connector as db
mydb=db.connect(host="localhost",user="root",passwd="12345",database="packages")
cursor=mydb.cursor()
cursor.execute("select * from hyderabad")
rec=cursor.fetchall()
for r in rec:
        print(r)
        
mydb.close()

