import csv
import pandas as pd

with open('data4.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# 使用pandas读取文件 (比较便捷)
df = pd.read_csv('data4.csv')
print(df)