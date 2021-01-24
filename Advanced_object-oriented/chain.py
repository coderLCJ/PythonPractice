class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):   # 必须写一个call函数 让实例可以直接调用 实现Chain().users('name')
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__


print(Chain().users('laity').repos)  # /users/michael/repos
# KEY: 第一步，返回了一个新的Chain1, 此时 path='users'
#      第二步，Chain1('laity')，即直接对实例进行调用，需要写call函数
#      这是与以下代码的区别
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


Chain().status.user.timeline.list
# 该步全都是调用不存在的属性，故只需写getattr即可，无需写call函数，因为并没有设计直接对实例进行方法调用
