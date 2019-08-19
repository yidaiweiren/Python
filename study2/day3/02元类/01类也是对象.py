'''

类也是对象
创建类的时候，python解释器相当于先执行一次类中的代码

'''
class Person(object):

    print("-----Person-test-----")

    def __init__(self):
        self.name = "abc"

print("100")
print("haha")

print(Person)   #可以打印出东西，类也是对象