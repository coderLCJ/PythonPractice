class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('name: %s score: %s' % (self.name, self.score))


stu1 = Student('Laity', '100')
stu1.print_score()
