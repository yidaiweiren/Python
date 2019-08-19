#-*-coding:utf-8-*- #声明编码
'''
    名片管理系统 ver0.1
1.添加一个新的名片
2.删除一个名片
3.修改一个名片
4.查询一个名片
5.退出
'''
#定义一个接收字典的列表
card_infors=[]


#1.打印功能提示
def print_menu():
    '''打印提示功能'''
    #可以使用help(print_menu)在ipython中查看具体功能
    print ("*#"*25)
    print ("名片管理系统 Ver 1.0".center(42))
    print ("一代伟人".rjust(42))
    print ("*#"*25)
    print ("1.添加一个新的名片")
    print ("2.删除一个名片")
    print ("3.修改一个名片")
    print ("4.查询一个名片")
    print ("5.查询所有名片")
    print ("6.退出")
    print ("*#"*25)

def add_new_card_infors():
    '''新建用户'''
    # 2-1.打印用户新建名片提示
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的QQ：")
    new_addr = input("请输入新的地址：")

    # 结合所学字典知识，这里适合使用字典存储数据
    # 定义一个空的字典
    new_infor = {}

    # 定义字典的键值，并让其值匹配相应的用户输入值
    new_infor["name"] = new_name
    new_infor["QQ"] = new_qq
    new_infor["addr"] = new_addr
    global card_infors
    card_infors.append(new_infor)   #card.infors为全局变量
    print(card_infors)

def find_card_infors():
    '''查询一个姓名'''

    global card_infors  #声明全局变量
    find_name = input("请输入要查找的姓名:")
    find_flag = 0  # 表示没有找到
    for temp in card_infors:
        if find_name == temp["name"]:
            print("name\t\tQQ\t\taddr")
            print("%s\t\t%s\t\t%s" % (temp['name'], temp['QQ'], temp['addr']))
            find_flag = 1  # 表示查到了
            break
    if find_flag == 0:
        print("查无此人")

def show_all_infors():
    '''显示所有的信息'''

    global card_infors

    print("name\tQQ\taddr")
    for temp in card_infors:
        print("%s\t%s\t%s" % (temp['name'], temp['QQ'], temp['addr']))

def main():
    '''完成对整个程序控制系统的封装'''
    print_menu()    #打印菜单

    #2.处理用户输入的值
    #num=int(input("请输入（1-5）的操作序号："))    #接收用户的输入，并转换为int

    while True:
        num = int(input("请输入（1-6）的操作序号："))  # 接收用户的输入，并转换为int
        if num==1:
            add_new_card_infors()
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4:
            find_card_infors()
        elif num==5:
            show_all_infors()
        elif num==6:
            break
        else:
            print ("输入的数字不正确，请重新输入（1-5）的数字")
            print ("*#"*25)

main()