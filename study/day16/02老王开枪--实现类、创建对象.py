#老王开枪框架

class Person(object):
    '''人的类'''
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name

class Gun(object):
    '''枪的类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name    #用来记录枪的类型

class Danjia(object):
    '''弹夹的类'''
    def __init__(self,max_num): #max_num:装子弹的个数
        super(Danjia,self).__init__()
        self.max_num = max_num  #用来记录装子弹的最大容量

class Zidan(object):
    '''子弹的类'''
    def __init__(self,sha_shang_li):
        super(Zidan,self).__init__()
        self.sha_shang_li = sha_shang_li    #这颗子弹的威力


def main():
    '''用来控制整个程序的流程'''


    #创建一个老王对象
    laowang = Person("老王")
    #创建一个枪对象
    ak47 = Gun("AK47")
    #创见一个弹夹对象
    dan_jia = Danjia(20)    #不同的弹夹，装子弹的个数不同
    #创建一些子弹
    zi_dan = Zidan(10)  #不同的子弹有不同的杀伤力

    #老王把子弹安装到弹夹中
    #老王.安装子弹到弹夹中
    laowang.anzhuang_zidan(dan_jia,zi_dan)

    #老王把弹夹安装到枪上
    #老王.弹夹安装到枪上

    #老王拿起枪

    #创建一个敌人

    #老王开枪打敌人
if __name__ == "__main__":
    main()