import functools
import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2020-1-1')


def log_(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_('execute')
def now2():
    print('2021-1-1')

# ------------------------------------------------
# test
# 测试

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %.4f ms' % (fn.__name__, end_time - start_time))
        return fn(*args, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')


# ------------------------------------------
# 同时支持有或无字符串参数，以及如何在函数运行前后打印链接文字

def log(temp):

    if not isinstance(temp,str):
        # 使用decorator后,func指向log(func)
        # 将更名后的'__name__'更改回原函数名称防止签名错误
        @functools.wraps(temp)
        def wrapper(*args,**kw):
            # #operations
            return temp(*args,**kw)
        return wrapper
    else:
        # 此时temp为一串str参数
        # new decorator
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(temp) # 打印字符串temp
                # operations
                return func(*args,**kw)
            return wrapper
        return decorator
