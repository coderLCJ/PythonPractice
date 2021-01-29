import os

def like(str1, str0):
    i, j = 0, 0
    while i < len(str0):
        if str0[i] == str1[j]:
            t = i
            while j < len(str1) and t < len(str0):
                if str0[t] != str1[j]:
                    break
                j += 1
                t += 1
            if j == len(str1):
                return True
            j = 0
        i += 1
    return False

def search(name):
    file_list = [x for x in os.listdir('.') if os.path.isdir(x)]    # 找出当前所有子目录
    # 先在当前目录寻找
    for i in os.listdir('.'):
        if os.path.isfile(i) and like(name, i):
            print(os.path.abspath(i))
    for i in file_list:
        for j in os.listdir(i):
            if like(name, j):
                print(os.path.abspath(i) + '\\' + j)


s = input('请输入要查找的文件名：')
search('test')