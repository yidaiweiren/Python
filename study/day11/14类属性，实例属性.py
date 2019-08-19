#类属性，实例属性
#类在程序当中也是一个变量，称为类对象
#在类中创建的对象，称为实例对象
#实例属性：和具有某个实例对象 有关系，并且一个实例对象和另外一个实例对象不共享属性
#类属性：类属性所属于类对象  并且多个实例对象之间，共享同一个类属性
class Tool(object):
    #定义一个类属性，注意这个是在init外边，不是属性，是类属性
    num = 0

    #方法
    def __init__(self,new_name):
        #这里叫做实例属性
        self.name = new_name
        Tool.num+=1

tool1 = Tool("铁锹")

tool2 = Tool("工兵铲")

tool3 = Tool("水桶")

print (Tool.num)
'''
结果:3
'''