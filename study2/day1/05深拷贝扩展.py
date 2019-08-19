#深拷贝扩展
'''
a = [11,22,33]
b = [44,55,66]
c = [a,b]
import copy
e = copy.deepcopy(c)    这里是递归的拷贝，c中有a、b，同时也将a、b内容拷贝
'''

a = [11,22,33]
b = [44,55,66]
c = [a,b]
import copy
e = copy.deepcopy(c)

print (id(c))
'''2123679162760'''
print (id (e))
'''2123631539016'''
a.append(44)

print (c[0])
'''[11, 22, 33, 44]'''
print (e[0])
'''[11, 22, 33]'''