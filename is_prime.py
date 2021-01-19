def odds():
    n = 3
    while True:
        yield n
        n += 2


def _div_(n):
    return lambda x: x % n > 0


def prime():
    yield 2
    it = odds()
    while True:
        n = next(it)
        yield n
        it = filter(_div_(n), it)


i = 0
k = 1
for i in prime():
    print(i)
    k += 1
    if k == 10:
        break
