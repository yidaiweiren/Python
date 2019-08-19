#类属性，实例属性

class Tool(object):
    def __init__(self,new_name):
        self.name = new_name

num = 0

tool1 = Tool("铁锹")
num+=1
print (num)

tool2 = Tool("工兵铲")
num+=1
print (num)

tool3 = Tool("水桶")
num+=1
print (num)

'''
结果：但不太符合面向对象开发原则
1
2
3
'''