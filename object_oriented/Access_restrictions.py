class Student(object):
    def __init__(self, name, score):
        self.__name = name  # __name私有变量 __name__特殊变量 _name 约定私有
        self.__score = score

    def get_name(self):
        return self.__name


bart = Student('test1', '100')
print(bart.get_name())
bart.__name = 'test2'   # 错误 相当于新增了一个实例变量
print(bart.__name)
print(bart.get_name())  # 内部的__name变量并没有变化

