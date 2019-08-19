#设计4s店
'''
需求
可以选择不同的车
但原来的方法太麻烦，添加一个车类，就得改Carstore中的代码，非常麻烦
解耦的好处：全部是模块化，一个升级，不会影响其他模块正常运行
可以选择其他牌子的车，以及车型
'''
#4s店这个类
class Store(object):
    def select_car(self):
        pass

    def order(self,car_type):
        return self.select_car(car_type)

#宝马4s店类
class BMWStore(Store):
    def select_car(self,car_type):
        return BMWFactory().select_car_by_type(car_type)

#宝马工厂类
class BMWFactory(object):
    def select_car_by_type(self,car_type):
        if car_type == "x6":
            return x6()
        elif car_type == "名图":
            return Mingtu


#现代4s店类
class Factory(Store):
    def select_car(self,car_type):
        return Factory().select_car_by_type(car_type)

#现代工厂类
class Factory(object):
    def select_car_by_type(self,car_type):
        pass
        '''
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu
        '''
#汽车类
class Car(object):
    def move(self):
        print("-----车在移动-----")
    def music(self):
        print("-----正在播放音乐-----")
    def stop(self):
        print("-----车停止-----")

class x6(Car):
    pass

class Mingtu(Car):
    pass

bmw_store = BMWStore()
bmw = bmw_store.order("x6")
bmw.move()
