import os
print(os.name)      # 系统名称
print(os.environ)   # 环境变量
print(os.getenv('PATH'))    # 获取环境变量
print(os.path.abspath('.'))    # 当前目录绝对路径

os.mkdir('mkdir')   # 新建目录
os.rmdir('mkdir')   # 删除目录

print(os.path.split('/Users/michael/testdir/file.txt'))     # 拆分目录
print(os.path.splitext('/Users/michael/testdir/file.txt'))      # 获取后缀
print(os.path.join('/Users/michael', 'testdir'))    # 拼接目录
# 合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# os.rename('test1.txt', 'test0.txt')
# os.remove('test0.txt')

L = [x for x in os.listdir('.') if os.path.isdir(x)]    # 显示当前目录下所有子目录 (.isfile()显示文件)
print(L)

