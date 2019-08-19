#-*-coding:utf-8-*-
#递归的问题
#切记什么时候要结束递归


#危险的案例
def test():
    print ("haha")
    test()

test()

#相当于死循环。