#实例方法，类方法，静态方法
#调用类方法，可以使用类的名字，还可以使用对象调用类方法（这个对象必须是这个类创建的）

class Game(object):
    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"


    #类方法
    @classmethod
    def add_num(cls):   #同self，相当于类方法中的self，cls用来接收类的引用
        cls.num = 100

    #静态方法
    @staticmethod
    def print_menu():   #静态方法，可以不需要参数
        print("-----------")
        print("开始游戏")
        print("结束游戏")
        print("-----------")


game = Game()
#Game.add_num()  #类名调用类方法
game.add_num()  #实例对象调用类方法（这个对象必须是这个类创建的）
print (Game.num)

Game.print_menu()  #通过类名调用类方法
game.print_menu()  #通过实例对象调用类方法（这个对象也必须是这个类创建的）