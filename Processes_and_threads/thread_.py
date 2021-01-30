import threading, time, random

def loop():
    print('%s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        print('Thread %s >>> %d' % (threading.current_thread().name, n))
        n += 1
        time.sleep(1)
    print('%s end' % threading.current_thread().name)


if __name__ == '__main__':
    print('MainThread is running')
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('MainThread end')
