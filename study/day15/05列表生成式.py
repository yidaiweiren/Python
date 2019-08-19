#列表生成式

#range函数复习
#range(起始数字，结尾数字，步长)

r = range(10,18)    #在python3中不好用，在python2中打印[10,11,12,13,14,15-使用Python操作数据库,16,17]
print (r)
'''
range(10, 18)
'''

#列表生成
a = [i for i in range(10,18)]   #注意for后面不用写“：”，for前面要加一个自身值
print (a)
'''
[10, 11, 12, 13, 14, 15-使用Python操作数据库, 16, 17]
'''
