

from collections import Iterator

print (isinstance("abc",Iterator))
#False

print (isinstance([],Iterator))
#False

print (isinstance({},Iterator))
#False

print (isinstance(100,Iterator))
#False

print (isinstance((x for x in range(10)),Iterator))     #为可迭代对象
#True