import json

def get_name():
    try:
        with open('name.json', 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet():
    name = get_name()
    if name:
        print(name)
    else:
        print('error')

greet()