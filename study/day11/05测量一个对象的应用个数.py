#测试一个对象的引用个数

#引入sys模块
import sys

class T():
    pass

t = T()

#调用getrefcount()方法来统计计数

print (sys.getrefcount(t))
'''
2       为什么是2，这就类似于linux中的grep，ps -aux | grep xxx,也同时会长生一个grep xxx的进程，然后内存计数相当于就是两个在调用
'''

tt = t
print (sys.getrefcount(t))
#3

del tt
print (sys.getrefcount(t))
#2

del t
print (sys.getrefcount(t))
#程序崩了，已经删完了，没有了