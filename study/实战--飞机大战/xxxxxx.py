class Dog(object):
    def __init__(self):
        pass

    def request(self,Num,Biaoqing):
        self.num = Num
        self.biaoqing = Biaoqing
        print (self.num,self.biaoqing)

    def get(self,num,biaoqing):
        self.num = num
        self.biaoqing = biaoqing
        #print(self.num)
        return self.request(self.num,self.biaoqing)



wangcai = Dog()

wangcai.get(111,"haha")