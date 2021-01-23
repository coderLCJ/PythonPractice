# --------------------------
# __str__, __repr__,  __len__
class Student(object):
    def __len__(self):
        return 10

    def __str__(self):
        return 'My name is student'

    def __repr__(self):
        return 'My name is student'
    # || __repr__ = __str__


bart = Student()
print(bart)     # My name is student

# --------------------------
# __iter__, __getitem__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration
        return self.a

    def __getitem__(self, n):   # 实现下标取元素
        if isinstance(n, int):  # 如果n是整数 则计算出下标对应的FIB值
            a, b = 0, 1
            for i in range(n):
                a, b = b, a + b
                i += 1
            return a
        elif isinstance(n, slice):  # 如果是切片，实现切片操作（未考虑step参数，负数参数）
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for j in range(stop):
                if j >= start:
                    L.append(a)
                a, b = b, a+b
            return L


f = Fib()
for k in f:
    print(k, ' ', end='')
print('\n----------------')
print(f[3], f[4])
print('----------------')
print(f[1:3])

# --------------------------
# __getattr__
class Person(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'age':   # 返回值
            return 18
        elif item == 'city':
            return lambda: 'Beijing'    # 返回函数
        # 若不抛出错误 则默认返回None
        raise AttributeError('Person object has no attribute %s' % item)


bart = Person('Bart')
print(bart.age)
print('----------------')
# __call__
class People(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is \'%s\'' % self.name)


lay = People('Lay')
lay()
# 通过callable()函数判断一个对象是否是“可调用”对象。
print(callable(lay))
print(callable(People))
print(callable(123))
