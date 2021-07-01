# -*- coding: utf-8 -*-
function_list = {
        1: ("入职", "您可以进入此功能内添加员工"),
        2: ("离职", "您可以进入此功能内删除员工"),
        3: ("修改", "您可以进入此功能内修改员工的信息"),
        4: ("查看", "您可以进入此功能查询所有的员工信息"),
        5: ("搜索", "您可以搜索指定的员工，查询他/她的信息"),
        6: ("退出", "退出系统")
    }

person_dict = {10000: ["小强", "男", "汉武时期人士"]}
while True:
    print("欢迎登陆人力资源管理系统>>>>")
    for key, value in function_list.items():
        print(f"{key}:{value}")
    chose = input("请输入您的选择编号>>>")
    if chose.isdigit():
        chose = int(chose)
        if 0 < chose <= 6:
            if chose == 6:
                print("系统退出~~~~")
                print("欢迎下次光临~~~~")
                exit()
            elif chose == 5:
                flag = True
                while flag:
                    person_num = input("请输入您要查询的员工编号>>>")
                    if person_num.isdigit():
                        person_num = int(person_num)
                        print("正在查询中，请稍后~~~~~~")
                        print(f"您查询的员工编号为{person_num}的员工信息如下：")
                        pre = person_dict.get(person_num, "抱歉,您查询的员工信息不存在！")
                        print(pre)
                        if pre:
                            chose = input(f"您可以选择重置员工{person_num}Y/N>>>")
                            if chose.isalpha() and chose.upper() == "Y":
                                person_dict[person_num] = None
                                flag = False
                                print("重置成功，请到修改页面重新更换")
                            elif chose.isalpha() and chose.upper() == "N":
                                print("跳转主页面中~~~~~~~~~~~~~~~~~")
                                flag = False
                            else:
                                print("输入错误，请重新输入，谢谢合作")
                        else:
                            flag = False
            elif chose == 4:
                flag = True
                while flag:
                    for key, value in person_dict.items():
                        print(f"员工编号:{key}\n员工信息:{value}")
                    chose = input(f"是否回到主页面Y/N>>>")
                    if chose.isalpha() and chose.upper() == "Y":
                        flag = False
                    else:
                        continue
            elif chose == 3:
                flag = True
                while flag:
                    for key, value in person_dict.items():
                        print(f"员工编号:{key}\n员工信息:{value}")
                    person_num = input(f"请输入您要修改员工信息的编号or输入exit,返回上一级>>>")
                    if person_num.isdigit():
                        person_num = int(person_num)
                        per = person_dict.get(person_num, "您输入的员工不存在！")
                        if per:
                            while True:
                                chose = input("请选择您要修改员工的什么信息？（姓名1、性别2、年龄3）or 回到上级页面/4>>>")
                                if chose.isdigit():
                                    chose = int(chose)
                                    if chose == 1:
                                        aa = input("请输入您要改为什么鬼？")
                                        person_dict[person_num][0] = aa
                                    elif chose == 2:
                                        aa = input("请输入您要改为什么鬼？")
                                        person_dict[person_num][1] = aa
                                    elif chose == 3:
                                        aa = input("请输入您要改为什么鬼？")
                                        person_dict[person_num][2] = aa
                                    else:
                                        break
                                else:
                                    print("输入错误，请重新输入！or 回到上级页面/4")
                        else:
                            flag = False
                            print(per)
                    elif person_num.isalpha() and person_num.upper() == "EXIT":
                        flag = False
                    else:
                        print("输入错误，请重新输入~~~")
            elif chose == 2:
                flag = True
                while flag:
                    for key, value in person_dict.items():
                        print(f"员工编号:{key}\n员工信息:{value}")
                    person_num = input(f"请输入您要删除员工信息的编号or输入exit,返回上一级>>>")
                    if person_num.isdigit():
                        person_num = int(person_num)
                        per = person_dict.get(person_num, "您输入的员工不存在！")
                        if per:
                            person_num = person_dict.pop(person_num)
                            print(f"您已经成功删除员工信息为：{person_num}的员工")
                        else:
                            print(per)
                            print("请重新输入")
                    elif person_num.isalpha() and person_num.upper() == "EXIT":
                        flag = False
                    else:
                        print("输入错误，请重新输入~~~")
            else:
                flag = True
                while flag:
                    lis1 = ["姓名", "性别", "出生年代"]
                    lis = []
                    for i in range(len(lis1)):
                        num = input(f"请输入您要添加的员工{lis1[i]}")
                        lis.append(num)
                    person_dict[max(person_dict.keys()) + 1] = lis
                    print(f"添加成功，您已经成功添加员工{max(person_dict.keys())}")
                    chose = input("是否继续添加？Y/N")
                    if chose.isalpha() and chose.upper() == "N":
                        flag = False
                    elif chose.isalpha() and chose.upper() == "Y":
                        continue
                    else:
                        print("输入错误，你还是继续添加吧~~~~")
        else:
            print("您的输入有误，请输入(1-6)选项")
    else:
        print("您的输入有误，请重新输入")

