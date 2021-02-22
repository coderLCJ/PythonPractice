import pymysql

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('create database spiders default character set utf8')
print(cursor.fetchone())
cursor.close()

