import csv


with open('data4.csv', 'w', newline='') as csvfile:  # newline=''不会空行
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Bob', 20])
    writer.writerow(['10002', 'Tom', 18])
    writer.writerow(['10003', 'Jordan', 29])
    writer.writerow(['10004', 'Peter', 24])

with open('data4.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')      # delimiter设置分隔符号
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Bob', 20], ['10002', 'Tom', 18], ['10003', 'Jordan', 29]]) # 一次写入多行 传入多维列表

# 写入字典 （写入中文需要指定编码方式
with open('data4.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Bob', 'age': '11'})    # 写入字典
    writer.writerow({'id': '10002', 'name': '阿健', 'age': '18'})
