#copy.copy
#深拷贝扩展
'''
a = [11,22,33]
b = [44,55,66]
c = [a,b]
import copy
e = copy.copy(c)    这里只拷贝第一层的c，里面的内容的引用没有拷贝
'''

a = [11,22,33]
b = [44,55,66]
c = [a,b]
import copy
e = copy.copy(c)

print (id(c))
'''1929134625480'''
print (id(e))
'''1929116103496'''
a.append(44)

print (c[0])
'''[11, 22, 33, 44]'''
print (e[0])
'''[11, 22, 33, 44]'''