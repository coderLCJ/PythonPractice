import threading
# 不加锁 多个线程会同时运行 可能造成数据计算错误

money = 0   # 存款
lock = threading.Lock()

def change(n):
    global money
    money = money+n
    money = money-n

def run(n):
    for i in range(2000000):
        lock.acquire()  # 首先需要获取锁
        try:
            change(n)
        finally:
            lock.release()  # 解锁


t1 = threading.Thread(target=run, args=(8,))
t2 = threading.Thread(target=run, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(money)
