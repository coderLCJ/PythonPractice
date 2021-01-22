from types import MethodType

class Student(object):
    pass

def age(self, age):
    self.age = age


stu = Student()
stu.name = 'Laity'  # 给实例绑定一个属性
print(stu.name)
stu.set_age = MethodType(age, stu)  # 给实例绑定一个方法 但对其他实例无效
stu.set_age(25)
print(stu.age)
Student.set_age = age   # 给Student类动态绑定一个方法 所有实例都可用

class Test(object):
    __slots__ = ('name', 'age')     # 特殊的__slots__变量，来限制该class实例能添加的属性
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
