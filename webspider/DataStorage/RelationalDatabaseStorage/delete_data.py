import pymysql

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age = 20'

sql = f'delete from {table} where {condition}'
try:
    cursor.execute(sql)
    print('successful')
    db.commit()
except:
    db.rollback()
    print('Failed')

db.close()