'''
斐波那契数列：第三个数等于前两个数之和
1，2，3，5，8···
'''

def createNum():
    a,b = 0,1
    for i in range(5):
        #print(a)
        print(b)
        a,b = b,a+b

createNum()