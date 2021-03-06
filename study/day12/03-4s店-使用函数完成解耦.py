#设计4s店
'''
可以选择不同的车
但原来的方法太麻烦，添加一个车类，就得改Carstore中的代码，非常麻烦
解耦的好处：全部是模块化，一个升级，不会影响其他模块正常运行
'''
#4s店这个类
class CarStore(object):
    def order(self,car_type):
        return select_car_by_type(car_type) #将car_type扔给函数select_car_by_type()执行，得到一个结果，return结果给order
        #相当于不用修改Carstore这个类了，而只需要修改select_car_by_type这个函数，相当于解耦

def select_car_by_type(car_type):
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