import pymysql


id = '20210004'
name = 'laity'
age = 22

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306, db='spiders')
cursor = db.cursor()

# 方法一（不推荐）
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, name, age))
    db.commit() # 只有commit后才可实现增删改查
    print('插入成功')
except:
    db.rollback()   # 数据回滚 相当于什么都没发生
    print('插入失败')

# 方法二（推荐，传入动态字典，插入方法无需改动）
data = {
    'id': '20211002',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
# join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
values = ','.join(['%s'] * len(data))   # 构造 '%s,%s,%s'
sql = f'INSERT INTO {table}({keys}) values({values})'   # {}内替换成相应字符串变量
# 也可写作'INSERT INTO {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()
'''
事务机制
原子性：事务是一个不可分割的工作单位，要么事务中的操作都做，要么都不做
一致性：事务必须使数据库从一个一致性状态走向另一个一致性状态
隔离性：一个事务的执行不能被其他事务干扰
永久性：事务一旦提交，对数据库的改变是永久性的
'''