#深拷贝、浅拷贝
'''
浅拷贝：
    a = [11,22,33]
    b = a
    只是相当于把a的引用给了b

深拷贝：
    导入拷贝模块
    import copy
    c = copy.deepcopy(a)
    这就相当于重新在内存中了一个c
'''

import copy
a = [11,22,33]
#浅拷贝
b = a
print (id(a))
print (id(b))
'''
2274474549768
2274474549768
'''
#深拷贝
c = copy.deepcopy(a)
print (id(a))
print (id(c))
'''
2274474549768
2274474549832
'''




