import pymysql
# -*- coding: utf-8 -*-

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306, db='spiders')
cursor = db.cursor()

# 方法一 简单更新
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (11, 'laity'))
    print('successful')
    db.commit()
except:
    print('Failed')
    db.rollback()

# 方法二 动态更新
data = {
    'id': '2021101',
    'name': 'laity',
    'age': 20
}
# 构造 sql = 'insert students(id, name, age) valuse(%s,%s,%s) on duplicate key update id=%s, nmae=%s, age=%s'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data.values()))
table = 'students'

sql = f'insert {table}({keys}) values({values}) on duplicate key update'    # on duplicate key update: 主键若存在 则执行更新操作
update = ','.join([' {key} = %s'.format(key=key) for key in data])
sql += update

try:
    cursor.execute(sql, tuple(data.values())*2)
    print('successful')
    db.commit()
except:
    print('Failed')
    db.rollback()

db.close()