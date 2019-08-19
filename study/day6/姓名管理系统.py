'''
            作者：一代伟人
    姓名管理系统
1.添加一个新的名字
2.删除一个名字
3.修改一个名字
4.查询一个名字
5.退出系统
'''
#1.打印功能提示
print ("#*"*25)
print ("姓名管理系统".center(42))
print ("作者:一代伟人".rjust(42))
print ("#*"*25)
print ("1.添加一个新的名字")
print ("2.删除一个名字")
print ("3.修改一个名字")
print ("4.查询一个名字")
print ("5.退出系统")
print ("#*"*25)


names = []

#3.根据用户选择，执行相关功能
#此模块只执行一次就结束程序，不符合开发需求，所以此处使用while循环来实现
#while True:相当于程序永远循环，除非有跳出
while True :
    # 2.获取用户选择信息
    num = int(input("请输入功能序号："))

    if num == 1:
        New_name = (input("请输入一个名字:"))
        # 3-1.创建一个接收用户名的列表
        # names = []  #这个方法可行，但是names的生命周期只有一次，下次在添加时，相当于初始化，还是一个空列表
        # 解决方案，将names移到if以外
        names.append(New_name)
        print(names)
    elif num == 2:
        Remove = (input ("请输入需要删除的名字:"))
        names.remove(Remove)
        print (names)
    elif num == 3:
        Update = (input ("请输入需要修改的用户:"))
        if Update in names:
            names_num = names.index(Update)     #获取下标/day6/find/
            New_update = (input ("请输入修改的新姓名:"))
            names[names_num] = New_update
            print (names)
        else:
            print ("用户不存在，请添加!")
    elif num == 4:
        Select = (input ("请输入需要查询的用户:"))
        if Select in names:
            print ("该用户存在")
            print (Select)      #存在直接输出接收的字符串，不存在直接else
        else:
            print ("用户不存在，请添加!")
    elif num == 5:
        print ("Bye-Bye!")
        break
    else:
        print("输入不正确，请输入数字（1-5）")
    print("#*" * 25)

'''
if num==1:
    new_name = (input ("请输入一个名字:"))
    #3-1.创建一个接收用户名的列表
    #names = []  #这个方法可行，但是names的生命周期只有一次，下次在添加时，相当于初始化，还是一个空列表
    #解决方案，将names移到if以外
    names.append(new_name)
    print (names)
elif num==2:
    pass
elif num==3:
    pass
elif num==4:
    pass
elif num==5:
    pass
else:
    print ("输入不正确，请输入数字（1-5）")
print ("#*"*25)
'''