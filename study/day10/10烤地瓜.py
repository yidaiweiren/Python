#烤地瓜

class SweetPotato:
    '''创建地瓜类'''
    def __init__(self):
        '''初始化属性'''
        self.cookedString="生的"  #买来是生的
        self.cookedlevel=0  #0表示生的 （烤的状态）
        self.condiments=[]  #佐料为字符串，且每次都相当于沾到地瓜上，所以使用列表保存
    def __str__(self):
        return "地瓜状态:%s(烤了%d分钟),当前添加的佐料有:%s"%(self.cookedString,self.cookedlevel,str(self.condiments))

    '''定义方法'''
    #创建一个“烤”的方法
    def cook(self,cooked_time):    #cookef_time:烤的时间

        self.cookedlevel+=cooked_time

        if self.cookedlevel>=0 and self.cookedlevel<3:
            self.cookedString="生的"
        elif self.cookedlevel>=3 and self.cookedlevel<5:
            self.cookedString="半生不熟"
        elif self.cookedlevel>=5 and self.cookedlevel<8:
            self.cookedString="熟了"
        elif self.cookedlevel>8:
            self.cookedString="烤糊了"

    #创建一个“调料”的方法
    def addCondiments(self,item):    #condiments:释义为：调料、佐料
        self.condiments.append(item)
#创建一个地瓜对象
di_gua=SweetPotato()
print (di_gua)

#调用“烤”的方法
di_gua.cook(1)
print (di_gua)
di_gua.cook(1)
print (di_gua)
di_gua.cook(1)
print (di_gua)
di_gua.addCondiments("盐")
di_gua.cook(1)
print (di_gua)
di_gua.cook(1)
print (di_gua)
di_gua.addCondiments("油")
di_gua.cook(1)
print (di_gua)
di_gua.addCondiments("十三香")
di_gua.cook(1)
print (di_gua)
di_gua.addCondiments("孜然")
di_gua.cook(1)
print (di_gua)
di_gua.cook(1)
print (di_gua)