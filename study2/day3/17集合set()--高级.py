
'''

交集:&
并集：|
差集：-
对称差集：^(上三角)
'''
a = "abcdef"
b = set(a)
print(b)

A = "bdfhuy"
B = set(A)
print(B)

#求交集
print(b&B)

#求并集(将b和B揉到一起，并且去重)
print(b|B)

#求差集(b减去B，再减去交集，“b中剩余的”)
print(b-B)

#对称差集（相当于“异或”除了b，B交集之外，b单独有的，和B单独有的，组成的集合）
print(b^B)