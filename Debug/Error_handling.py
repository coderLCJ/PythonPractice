import logging
# try except finally
def fun():
    try:
        print('try....')
        a = 10/int('a')
        print('end')
    except ValueError as e:
        print('error', e)
    except ZeroDivisionError as e:
        print('error:', e)
    else:
        print('no error')
    finally:
        print('finally...')
    print('END')


# 跨级处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('a')
    except Exception as e:
        print('Error:', e)
        logging.exception(e)    # 记录错误 并且正常退出
    finally:
        print('finally...')


main()
