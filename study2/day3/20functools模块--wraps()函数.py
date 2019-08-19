'''

wraps():使用装饰器时，有一些细节需要被注意。
例如：被装饰后的函数其实已经是另外一个函数了，（函数名等函数属性会发生改变）
'''

import functools
def note(func):
    "note function"
    def warpper():
        "warpper function"
        print("note something")
        return func()
    return warpper

@note
def test():
    "test function"
    print("I an test")

test()
print(test.__doc__)