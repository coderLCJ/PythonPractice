html = '''
<html>

<p>Hello World</p>

</html>
'''
with open('data1.txt', 'w', encoding='utf-8') as f:
    f.write(html)    # 自动关闭文件 不需要手动close