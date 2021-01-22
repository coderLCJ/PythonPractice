class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Pig(Animal):
    def run(self):
        print('Pig is running')

class Run(Animal):  # 不是必须传入Animal 只要有run方法的类都可以 称为‘鸭子类型’
    def start(self, Animal):
        Animal.run()

class Duck(object):  # 鸭子类型
    def run(self):
        print('Duck type')


test1 = Dog()
test2 = Pig()
test3 = Duck()
run_test = Run()
run_test.start(test1)
run_test.start(test2)
run_test.start(test3)
