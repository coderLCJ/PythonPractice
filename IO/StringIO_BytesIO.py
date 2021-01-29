from io import StringIO
from io import BytesIO
f = StringIO()
f.write('Hello StringIO')
print(f.getvalue())

p = StringIO('Hello World\n123\n345')
while True:
    s = p.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO与StringIO类似 只是读写的是二进制数据
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
