class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=ListMetaclass):
    pass


L = Mylist()
L.add(1)
L.add(2)
print(L)
