f = open('test.txt', 'r')
print(f.read())
f.close()
# 不用主动使用close()
with open('test.txt', 'r') as p:
    print(p.read(2))

# 二进制文件（图片、视频）
f1 = open('test.jpg', 'rb')
f2 = open('test.txt', 'rb', encoding='gbk', errors='ignore')



