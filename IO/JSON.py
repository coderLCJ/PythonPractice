import json
d = dict(name='laity', age=19)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str)
print(s)
