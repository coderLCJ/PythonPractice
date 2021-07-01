# -*- coding: utf-8 -*-
f = open('D://score1.txt', encoding='utf8')
p = open('D://score2.txt', 'w', encoding='utf8')

text = f.read()
info = []   # 存放标题
id = []
name = []
score = []
sumScore = []
course1 = []
course2 = []
course3 = []
i = 0
for line in text.split('\n'):
    temp = 0
    for key in line.split(','):
        if i < 5:
            info.append(key)
        else:
            if i % 5 == 0:
                id.append(key)
            elif i % 5 == 1:
                name.append(key)
            else:
                temp += int(key)
                score.append(int(key))
                if i % 5 == 2:
                    course1.append(int(key))
                if i % 5 == 3:
                    course2.append(int(key))
                if i % 5 == 4:
                    course3.append(int(key))
        i += 1
    if i > 5:
        sumScore.append(temp)

print('==================================')
print('语文最高分：', max(course1), '语文最低分：', min(course1), '语文平均分：', sum(course1)/len(id))
print('数学最高分：', max(course2), '数学最低分：', min(course2), '数学平均分：', sum(course2)/len(id))
print('英语最高分：', max(course3), '英语最低分：', min(course3), '英语平均分：', sum(course3)/len(id))

print('==================================')
print('所有同学总分为')
for i in info:
    p.write(i + ',')
    print(i, end=',')
print('总分')
p.write('总分\n')
j = 0
for i in range(len(id)):
    print(id[i], name[i], score[j], score[j+1], score[j+2], sumScore[i])
    p.write(id[i] + ',')
    p.write(name[i] + ',')
    p.write(str(score[j]) + ',')
    p.write(str(score[j+1]) + ',')
    p.write(str(score[j+2]) + ',')
    p.write(str(sumScore[i]) + '\n')
    j += 1
print('==================================')
print('文件已保存到D://score2.txt中')
f.close()
p.close()