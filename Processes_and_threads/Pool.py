from multiprocessing import Pool
import os, time, random
# 使用Pool创建大量子进程
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('time %s run %.2f seconds' % (name, end-start))


if __name__ == '__main__':
    print('Parent process %s start' % os.getpid())
    p = Pool(4)     # 创建四个子进程
    # Pool的默认大小是CPU的核数 因此前4个子进程瞬间执行 第5个需要等前4个开始之后再执行
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('wait for all subprocess done...')
    p.close()
    p.join()    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
    print('END')
