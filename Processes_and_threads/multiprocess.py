from multiprocessing import Process
import os

def run_child(name):
    print('Child process \'%s\' is running (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process \'%s\' is running (%s)' % ('main', os.getpid()))
    p = Process(target=run_child, args=('test',))
    print('Child process will start....')
    p.start()       # 启动子进程
    p.join()        # 等待子进程结束后再继续往下运行
    print('END')
