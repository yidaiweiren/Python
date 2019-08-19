'''

In [1]: from collections import Iterable

In [2]: isinstance("abc",Iterable)
Out[2]: True

In [3]: isinstance([],Iterable)
Out[3]: True

In [4]: isinstance({},Iterable)
Out[4]: True

In [5]: isinstance(100,Iterable)
Out[5]: False
'''

from collections import Iterable

print (isinstance("abc",Iterable))
#True

print (isinstance([],Iterable))
#True

print (isinstance({},Iterable))
#True

print (isinstance(100,Iterable))
#False