import pymysql

db = pymysql.connect(host='localhost', user='root', password='19990806', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age > 1'

try:
    cursor.execute(sql)
    # cursor.fetchall() һ��ȡȫ�� ��ȡ��ָ��ָ��ĩβ
    # �Ƽ��������
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    print('successful')
except:
    print('Failed')

db.close()