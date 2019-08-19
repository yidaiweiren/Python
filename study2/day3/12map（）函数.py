'''
map函数
'''

#map（）接收一个参数
ret = map(lambda x:x*x,[1,2,3,4])
'''
在列表中取一个数，给x，然后x*x，打印结果
'''

for tmp in ret:
    print(tmp)

print("*"*20)

#map接收两个参数
i = map(lambda x,y:x+y,[1,2,3,4],[1,2,3,8])

for j in i:
    print(j)

print("*"*20)

#map（）混合计算
def f1(a,b):
    return(a,b)

l1 = [0,1,2,3,4,5,6]
l2 = ['sun','m','t','w','t','f','s']
l3 = map(f1,l1,l2)
print(list(l3))