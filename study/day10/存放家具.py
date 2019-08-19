#存放家具
#需要将床这个对象扔进房子
class Home:
    def __init__(self,new_master_name,new_area,new_info,new_addr):
        '''初始化房子的属性'''
        self.master_name = new_master_name  #房主名称
        self.area = new_area    #房子的总面积
        self.left_area = new_area   #房子的剩余可用面积
        self.info = new_info    #房子的户型
        self.addr = new_addr    #房子的位置
        self.contain_items = []     #创建接收物品的列表

    def __str__(self):  #此处若不加__str__，那么将会打印出对象所在内存中的位置信息
        '''获取对象的描述信息(属性)'''
        return "%s家的房子的总面积是：%d平米；房子的剩余可用面积是：%d平米；房子的户型是：%s；房子的位置是：%s。\n当前房子中的家具有%s\n"%(self.master_name,self.area,self.left_area,self.info,self.addr,str(self.contain_items))

    def add_item(self,item):     #添加物品
        '''添加物品的方法'''
        #self.left_area -= item.area     #item已经引用了这张床，相当于item就是床，那么直接可以调用床的area属性
        #self.contain_items.append(item.name)

        self.left_area -= item.get_area()  #定义一个get方法获取属性的值，在工作中，直接获取不安全，有些东西不能让获取，所以将直接获取修改为get方法
        self.contain_items.append(item.get_name())
class Bed:
    def __init__(self,new_name,new_area):
        '''初始化床的属性'''
        self.name = new_name    #床的名字
        self.area = new_area    #床的面积

    def __str__(self):
        '''获取对象的描述信息(属性)'''
        return "添加了一个床，床的名字是：%s；床的面积是：%d平米。"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name
fangzi = Home("一代伟人",129,"三室一厅","陕西省 西安市 高新区 **小区 666号")
print (fangzi)

bad1 = Bed("双人床",12)
print (bad1)


fangzi.add_item(bad1)   #房子调用添加物品方法，这里添加一个床
print (fangzi)

bad2 = Bed("席梦思",7)
print (bad2)


fangzi.add_item(bad2)   #房子调用添加物品方法，这里添加一个床
print (fangzi)


#创建一个类，可以支持创建n多个对象，且每个对象互不干扰，这就是牛逼之处
jia = Home("崔渊博",130,"四室一厅","西安")
jia.add_item(bad2)
print (bad2)
print (jia)