#==、is的区别
'''
==:仅仅判断这个值相等
is：判断拥有者是否相同

举例：
我的iphone和你的iphone 是相同的手机
即：iphone == iphone
但是，我不是你
即：iphone is iphone
结果为：True

'''
a = [11,22,33]
b = [11,22,33]

print (a == b)  #True
print (a is b)  #False

#扩展
c = a
print (a is c)  #True
#此处a和b指向同一片内存空间，相当于我自己有一个小名，这个iphone属于我，即大名小名都属于，所以为True


#例外 -5~125之间的数都是相同的
d = 100
e = 100
print (d == e)  #True
print (d is e)  #True
