import mysql.connector
from main import row
from main import list1
from pprint import pprint

mydb=mysql.connector.connect(
host="113.172.178.64",
user="root",
password="Lmao!123",
auth_plugin='mysql_native_password',
database='test',
) 
mycursor=mydb.cursor()
# # mycursor.execute("SHOW DATABASES")
# # myresult=mycursor.fetchall()
# # for x in myresult:
# #     print(x)

for x in list1:
    print(x)

# sql= "INSERT INTO stocks (bumber, daddy,sus) VALUES (%s,%s,%s)"
# y=mycursor.executemany(sql, [(x,) for x in list1])
# print(y)
# mydb.commit()


