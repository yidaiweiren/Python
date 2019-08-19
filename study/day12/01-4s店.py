#设计4s店

#4s店这个类
class CarStore(object):
    def order(self,money):
        if money>50000:
            return Car()

#汽车类
class Car(object):
    def move(self):
        print("-----车在移动-----")
    def music(self):
        print("-----正在播放音乐-----")
    def stop(self):
        print("-----车停止-----")

car_store = CarStore()
car = car_store.order(100000)     #order:释义为预定
car.move()
car.music()
car.stop()