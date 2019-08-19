#给程序传递参数

import sys

print (sys.argv)    #sys.argv用来接收用户执行时给程序传递的参数，以列表形式保存

name = sys.argv[1]
print ("热烈欢迎，%s的到来"%name)

'''
C:\\Users\Administrator>python D:/PycharmProjects/Python/study/day15/04给程序传递参数.py a b c d        运行时给了几个参数
['D:/PycharmProjects/Python/study/day15/04给程序传递参数.py', 'a', 'b', 'c', 'd']      程序接收到的参数，如果没参数，就打印本身文件名
热烈欢迎，老王的到来

实战
C:\\Users\Administrator>python D:/PycharmProjects/Python/study/day15/04给程序传递参数.py 一代伟人
['D:/PycharmProjects/Python/study/day15/04给程序传递参数.py', '一代伟人']
热烈欢迎，一代伟人的到来

'''