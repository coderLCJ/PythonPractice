from  collections import OrderedDict

stu = OrderedDict()
stu['Tom'] = 1234;
stu['Jack'] = 5678;

for k, v in stu.items():
    print(k, ' ', v)
