import types

class Test(object):
    def __init__(self):
        self.x = 1
        self.y = 2

    def test(self):
        print('test function')

def Fun():
    print('Function')


t1 = Test()
print(type(t1))  # type(name) 判断对象所属类 返回对应的Class类型
print(type(123) == type('123'))
# type也可以判断对象是否是函数
print(type(Fun) == types.FunctionType)

# 用type判断的 也可以用instance函数
print(isinstance([1, 2, 3], (list, tuple)))     # 判断是否属于括号后面的某一种

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
# print(dir('ABC'))

# getattr() setattr() hasattr()
print(hasattr(t1, 'x'))
