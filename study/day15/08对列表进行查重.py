#对列表进行查重

a = [11,22,33,44,11,22,33]

c = set(a)

print (c)

#再转会列表
b = list(c)

print (b)
'''
{33, 11, 44, 22}
[33, 11, 44, 22]
'''

#方法二
d = []
for i in a:
    if i not in d:
        d.append(i)

print (d)
'''
[11, 22, 33, 44]
'''

