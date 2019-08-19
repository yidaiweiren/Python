'''

属性拦截器
原来定义以后,直接可以访问这个方法,而现在加了getattribute方法后,访问被重定向到__getattribute__这个方法中
object.__getattribute__是当上面判断不满足是,返回到原来的方法中执行的方式
在__getattribute__方法中禁止使用self.xx
'''
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器,打log
    def __getattribute__(self,obj):
        print('=====1>%s'%obj)
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            temp = object.__getattribute__(self,obj)
            print('=====2>%s'%str(temp))
            return temp

    def show(self):
        print('this is Itcast')


s = Itcast('python')
print(s.subject1)
print(s.subject2)
s.show()
'''
1.先获取show属性对应的结果,结果应该是一个方法
2.方法()
'''