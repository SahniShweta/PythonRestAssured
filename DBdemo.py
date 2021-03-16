import mysql.connector
from utilities.configurations import *
# conn = mysql.connector.connect(host='localhost', database= 'APIDevelop', user='root', password= 'Gaadi@81')

conn = getConnection()
# print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo;')
# row = cursor.fetchone()
# print(row)
rowAll = cursor.fetchall()
# print(rowAll)
# print(row[2])
sum1 = 0
for row in rowAll:
    sum1 = sum1 + row[2]

print(sum1)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("US","Jmeter")
cursor.execute(query,data)
conn.commit()
conn.close()



