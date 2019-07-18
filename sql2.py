import mysql.connector
from _ctypes import buffer_info

my=mysql.connector.connect(user="root",
                           host="localhost",
                           password="root")
print(my)
cursor=my.cursor(buffered=True)
#cursor.execute("create database nidhi")
cursor.execute("use nidhi")
# cursor.execute("CREATE table persons(personid int NOT NULL AUTO_INCREMENT,LastName varchar(255),FirstName varchar(255),Age int(255),PRIMARY KEY (Personid))")

#cursor.execute("insert into persons values(1,'gupta','ram',20)")
# my.commit()
# #cursor.execute("insert into persons values(null,'kapoor','vijay',20)")
# my.commit()
# insert_query="insert into persons value(null,%s,%s,%s)"
# data=[('khayap','shivani',21),('jain','nidhi',20),('goyal','shivani',20)]
# cursor.executemany(insert_query,data)
# my.commit()
cursor.execute("use nidhi")
cursor.execute("select * from persons")
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.fetchone())
# for record in cursor in cursor.fetchall():
#     print("record found",