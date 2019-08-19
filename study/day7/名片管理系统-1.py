'''
    名片管理系统 ver0.1
1.添加一个新的名片
2.删除一个名片
3.修改一个名片
4.查询一个名片
5.退出
'''
#1.打印功能提示
print ("*#"*25)
print ("名片管理系统 Ver 1.0".center(42))
print ("一代伟人".rjust(42))
print ("*#"*25)
print ("1.添加一个新的名片")
print ("2.删除一个名片")
print ("3.修改一个名片")
print ("4.查询一个名片")
print ("5.退出")
print ("*#"*25)
#2.处理用户输入的值
#num=int(input("请输入（1-5）的操作序号："))    #接收用户的输入，并转换为int

#定义一个接收字典的列表
card_infors=[]


while True:
    num = int(input("请输入（1-5）的操作序号："))  # 接收用户的输入，并转换为int
    if num==1:
        #2-1.打印用户新建名片提示
        new_name=input("请输入新的名字：")
        new_qq=input("请输入新的QQ：")
        new_addr=input("请输入新的地址：")

        #结合所学字典知识，这里适合使用字典存储数据
        #定义一个空的字典
        new_infor={}

        #定义字典的键值，并让其值匹配相应的用户输入值
        new_infor["name"]=new_name
        new_infor["QQ"]=new_qq
        new_infor["addr"]=new_addr
        card_infors.append(new_infor)
        print(card_infors)

        #判断用户是否存在
        '''
        if new_name in card_infors:
            print ("%d-存在"%new_name)
        else:

            #用户输入的信息以获取，现在使用append（）方法写入列表 append day6/
            card_infors.append(new_infor)
            print (new_infor)
            print (card_infors)
        '''
        #使用for尝试遍历
        for card_value in card_infors:
            #print (card_value)
            for new_card_value in card_value.values():
                #print (new_card_value)
                if new_name==new_card_value:
                    print ("存在")

                else:
                    # 用户输入的信息以获取，现在使用append（）方法写入列表 append day6/
                    #card_infors.append(new_infor)
                    print(new_infor)
                    #print(card_infors)
                break

    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        pass
    elif num==5:
        pass
    else:
        print ("输入的数字不正确，请重新输入（1-5）的数字")
        print ("*#"*25)

