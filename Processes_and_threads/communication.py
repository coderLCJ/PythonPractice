from multiprocessing import Process, Queue
import os, random, time

# 写数据
def write(q):
    print('Write process %s is running' % os.getpid())
    for value in ['A', 'B', 'C']:
        q.put(value)
        print('push %s into queue' % value)
        time.sleep(random.random())

# 读数据
def read(q):
    print('Read process %s is running' % os.getpid())
    while True:
        value = q.get(True)
        print('Get value %s from queue' % value)
        time.sleep(random.random())


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

