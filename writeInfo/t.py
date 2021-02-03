import os, time

#os.system('python write.py')

while True:
    localtime = time.localtime(time.time())
    # print("本地时间为 :", localtime)
    # print(localtime.tm_hour)
    if localtime.tm_sec%2 == 1:
        print(localtime.tm_sec)
