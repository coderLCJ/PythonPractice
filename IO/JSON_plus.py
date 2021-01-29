import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student_to_dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# class转换为json
s = Student('laity', 15, 386)
print(json.dumps(s, default=student_to_dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))   # 偷懒写法 class内不能有__slots__

# JSON反序列化为一个Student对象实例
def dict_to_student(d):
    return Student(d['age'], d['score'], d['name'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
p = json.loads(json_str, object_hook=dict_to_student)
print(p.name, p.age, p.score)
