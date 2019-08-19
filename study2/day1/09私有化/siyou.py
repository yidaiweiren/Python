num = 100
_num = 200
__num = 300


'''
实际证明：只有有下划线的变量或者属性或者方法都不能在外部调用

In [2]: from siyou import *

In [3]: num
Out[3]: 100

In [4]: _num
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-6dd7111d6a95> in <module>
----> 1 _num

NameError: name '_num' is not defined

In [5]: __num
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-f0ba2c4a214a> in <module>
----> 1 __num

NameError: name '__num' is not defined
'''


'''
如果使用import名，直接是可以使用的
In [6]: import siyou

In [8]: siyou.num
Out[8]: 100

In [9]: siyou._num
Out[9]: 200

In [10]: siyou.__num
Out[10]: 300
'''