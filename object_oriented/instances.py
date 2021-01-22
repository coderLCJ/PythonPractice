class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = Student('Bart', 99)
lisa = Student('Lisa', 88)
bart.age = 100
print(bart.age)     # 可和任意实例变量绑定
print(lisa.age)     # 错误 'Student' object has no attribute 'age'

