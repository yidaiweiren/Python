'''
reduce()函数：对参数序列中的元素进行累积
需要引入函数库：from functools import reduce
'''
from functools import reduce

#案例1
ret = reduce(lambda x,y:x+y,[1,2,3,4])
print(ret)
'''
先将1给x，然后将2给y，计算结果为3
将计算结果3给x，将列表中的3给y，依次累积
'''


#执行过程详解
tmp = reduce(lambda x,y:x+y,['aa','bb','cc'],'dd')
print(tmp)
'''
ddaabbcc
先将dd给x，然后将aa给y
然后得到ddaa在给x，bb给y
'''