#查看对象的引用计数

import sys

a = "hello word"
print(sys.getrefcount(a))