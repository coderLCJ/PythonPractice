import csv

with open('data4.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Bob', 20])
    writer.writerow(['10002', 'Tom', 18])
    writer.writerow(['10003', 'Jordan', 29])