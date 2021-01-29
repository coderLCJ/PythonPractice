import pickle
d = dict(name='laity', age=19)
f = open('pickle.txt', 'wb')
pickle.dump(d, f)   # 写入文件
f.close()

p = open('pickle.txt', 'rb')
d = pickle.load(p)  # 读取文件
print(d)
