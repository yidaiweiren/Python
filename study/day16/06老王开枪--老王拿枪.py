#老王开枪框架

class Person(object):
    '''人的类'''
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None     #用来保存枪对象的引用
        self.hp = 100       #定义当前用户的血量

    #创建安装子弹方法
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        '''把子弹装到弹夹里'''
        #self.dan_jia_temp = dan_jia_temp
        #self.zi_dan_temp = zi_dan_temp
        #弹夹.保存子弹(子弹)
        dan_jia_temp.baocun_zidan(zi_dan_temp)  #保存功能需要在弹夹中实现

    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        '''把弹夹安装到枪上'''
        #枪.保存弹夹（弹夹）
        gun_temp.baocun_danjia(dan_jia_temp)    #保存弹夹的功能需要在枪中实现

    def naqiang(self,gun_temp):
        '''拿起一把枪'''
        #老王.保存枪（枪）
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return "%s的血量为：%d，他手上有枪,%s"%(self.name,self.hp,self.gun)
        else:
            return "%s的血量为：%d，他手上没有枪。"%(self.name,self.hp)

class Gun(object):
    '''枪的类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name    #用来记录枪的类型
        self.danjia = None  #用来记录弹夹对象的引用

    def baocun_danjia(self,dan_jia_temp):   #注：一个对象永远不可能保存另一个对象。所以此处可以找一个属性保存枪与弹夹的引用
        '''用一个属性来保存枪对象与这个弹夹对象的应用'''
        self.danjia = dan_jia_temp

    def __str__(self):
        #判断枪是否安装有弹夹
        if self.danjia:
            return "枪的信息为：%s，%s。"%(self.name,self.danjia)
        else:
            return "枪的信息为：%s，这把枪没有安装弹夹。"%(self.name)

class Danjia(object):
    '''弹夹的类'''
    def __init__(self,max_num): #max_num:装子弹的个数
        super(Danjia,self).__init__()
        self.max_num = max_num  #用来记录装子弹的最大容量
        self.zidan_list = []     #用来记录所有的子弹的引用

    def baocun_zidan(self,zi_dan_temp):    #注：一个对象永远不能保存另一个对象。所以此处可以找一个属性来保存弹夹与子弹的引用
        '''将这颗子弹保存'''
        self.zidan_list.append(zi_dan_temp)     #将引用放到列表，也就是说将子弹压入弹夹

    def __str__(self):
        return "弹夹的信息为:%d/%d"%(len(self.zidan_list),self.max_num)

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
    for i in range(15):
        zi_dan = Zidan(10)  #不同的子弹有不同的杀伤力

        #老王把子弹安装到弹夹中
        #老王.安装子弹到弹夹中（弹夹，子弹）
        laowang.anzhuang_zidan(dan_jia,zi_dan)  #谁调用这个方法，就把这个方法放到谁的类下面，也就是说放到Person下

        #统计安装过程
        i+=1
        print("安装第%d颗子弹"%i)

    #老王把弹夹安装到枪上
    #老王.弹夹安装到枪上（枪，弹夹）
    laowang.anzhuang_danjia(ak47,dan_jia)

    #测试弹夹的信息
    print (dan_jia)
    #测试枪的信息
    print (ak47)
    #老王拿起枪
    #老王.拿枪(ak47)
    laowang.naqiang(ak47)

    #测试老王对象
    print (laowang)

    #创建一个敌人


    #老王开枪打敌人
if __name__ == "__main__":
    main()