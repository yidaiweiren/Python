#设计4s店
'''
可以选择不同的车
'''
#4s店这个类
class CarStore(object):
    #cals下的order方法，与车型的类出现耦合，一个有问题程序就会崩，而且修改类风险太大，不推荐，所以请参考day12/03-解耦
    def order(self,car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu

#汽车类
class Car(object):
    def move(self):
        print("-----车在移动-----")
    def music(self):
        print("-----正在播放音乐-----")
    def stop(self):
        print("-----车停止-----")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

car_store = CarStore()
car = car_store.order("索纳塔")     #order:释义为预定
car.move()
car.music()
car.stop()