#使用continue跳出当前次的循环
#break直接结束整个while的循环生命
#continue直结束“结果成立”当前次，然后跳出继续执行
i = 1
while i<=5:
    i+=1
    print ("****")
    if i==3:
        break   #使用break结束所有循环
    print (i)

print("="*20)

j = 1
while j<=5:
    j+=1
    print ("####")
    if j==3:
        continue    #使用continue结束当次循环
    print (j)

#结果
'''
****
2
****
====================
####
2
####
####
4
####
5
####
6

'''
