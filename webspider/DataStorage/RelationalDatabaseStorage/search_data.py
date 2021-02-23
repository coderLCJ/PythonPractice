import pymysql

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age > 1'

try:
    cursor.execute(sql)
    # cursor.fetchall() 一次取全部 读取完指针指向末尾
    # 推荐逐条输出
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    print('successful')
except:
    print('Failed')

db.close()