#for-else-应用
#事实证明，在for循环中加else，不管循环执不执行，最后都要执行else

str=['11','22','33','44']
str1=[]

for i in str:
    print (i)
else:
    print ('='*10)
'''
循环执行完打印横杠，接着往下看
11
22
33
44
==========
'''

for j in str1:
    print (j)
else:
    print ('='*10)
'''
事实证明，在for循环中加else，不管循环执不执行，最后都要执行else
==========
'''