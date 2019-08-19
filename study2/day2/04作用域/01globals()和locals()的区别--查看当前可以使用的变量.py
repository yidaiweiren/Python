'''
globals()   全局可用的变量
In [1]: a = 100

In [2]: b = 200

In [3]: globals()
Out[3]:
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['', 'a = 100', 'b = 200', 'globals()'],
 '_oh': {},
 '_dh': ['D:\\PycharmProjects\\Python\\study2\\day1\\09私有化'],
 'In': ['', 'a = 100', 'b = 200', 'globals()'],
 'Out': {},
 'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x000001B30AE3F828>>,
 'exit': <IPython.core.autocall.ExitAutocall at 0x1b30ae5ab70>,
 'quit': <IPython.core.autocall.ExitAutocall at 0x1b30ae5ab70>,
 '_': '',
 '__': '',
 '___': '',
 '_i': 'b = 200',
 '_ii': 'a = 100',
 '_iii': '',
 '_i1': 'a = 100',
 'a': 100,
 '_i2': 'b = 200',
 'b': 200,
 '_i3': 'globals()'}

'''

'''
locals()    局部可用的变量
In [1]: def test():
   ...:     i = 1
   ...:     j = 3
   ...:     print(locals())
   ...:
In [3]: test()
{'i': 1, 'j': 3}
'''