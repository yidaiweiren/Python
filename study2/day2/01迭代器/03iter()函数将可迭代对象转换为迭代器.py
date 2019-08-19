

from collections import Iterator

print (isinstance(iter("abc"),Iterator))
#True

print (isinstance(iter([]),Iterator))
#True

print (isinstance(iter({}),Iterator))
#True

print (isinstance(100,Iterator))
#False

print (isinstance((x for x in range(10)),Iterator))     #为可迭代对象
#True