import mysql.connector
from _ctypes import buffer_info

my=mysql.connector.connect(user="root",
                           host="localhost",
                           password="root")
cursor=my.cursor(buffered=True)
cursor.execute("use user")
cursor.execute("select * from user_d")
print(cursor.fetchall())
for record in cursor.fetchall():
    print("Record found",record)

#cursor.execute("CREATE table Persons (Personid int
# NOT NULL AUTO_INCREMENT, LastName varchar(255) NOT NULL,FirstName varchar(255),Age int(255),
# PRIMARY KEY (Personid))")
#insert_query="insert into Persons values(1,'Lname','Fname',34)"
insert_query="insert into Persons values(null,'Lname','Fname',34)"
cursor.execute(insert_query)
insert_query="insert into Persons values(null,%s,%s,%s)"
data=[("l","m",5),
       ("k","p",7)]
cursor.executemany(insert_query,data)


my.commit()