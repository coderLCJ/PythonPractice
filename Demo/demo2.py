class Car():
    def __init__(self, name, year):
        self.name = name
        self.year = year

class elccar(Car):
    def __init__(self):
        super().__init__('audi', 2021)

c = elccar()
print(c.name)
