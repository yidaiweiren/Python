#定义--使用函数
#模拟名片管理系统
#简单打印几个三角形


#定义一个函数,专业角度来讲称为“封装”
def print_menu():
    print ("*"*30)
    print ("xxx系统")
    print ("1.xxx")
    print ("2.xxx")
    print ("*"*30)


def print_sanjiaoxing():
    print ("*")
    print ("*"*2)
    print ("*"*3)
    print ("*"*4)

#调用这个函数，只需要写函数名（），即可调用执行
print_menu()

'''
******************************
xxx系统
1.xxx
2.xxx
******************************
'''

''' 
这个位置，这种方式也可以写，没问题，不过显示不专业，函数定义最好放在一起，下边任意位置调用即可
def print_sanjiaoxing():
    print ("*")
    print ("*"*2)
    print ("*"*3)
    print ("*"*4)
'''

print_sanjiaoxing()

'''
*
**
***
****
'''