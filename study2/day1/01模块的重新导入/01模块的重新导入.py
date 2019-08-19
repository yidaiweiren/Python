#01模块的重新导入
'''
导入一个模块时，系统会在sys.path中读取路径，然后去相应路径下找模块，一个路径找不到，就去下一个，直到找到或者没找到报错。
sys.path是一个列表，如果后期需要导入其他路径的模块，可以将路径直接写入sys.path这个列表
'''
import sys
print (sys.path)
'''
['D:\\PycharmProjects\\Python\\study2\\day1', 'D:\\PycharmProjects\\Python', 'D:\\python\\Anaconda3\\python37.zip', 'D:\\python\\Anaconda3\\DLLs', 'D:\\python\\Anaconda3\\lib', 'D:\\python\\Anaconda3', 'D:\\python\\Anaconda3\\lib\\site-packages', 'D:\\python\\Anaconda3\\lib\\site-packages\\pymysql-0.9.3-py3.7.egg', 'D:\\python\\Anaconda3\\lib\\site-packages\\win32', 'D:\\python\\Anaconda3\\lib\\site-packages\\win32\\lib', 'D:\\python\\Anaconda3\\lib\\site-packages\\Pythonwin', 'D:\\PyCharm 2018.3.5\\helpers\\pycharm_matplotlib_backend']
'''

#给sys.path在添加一个/home路径
sys.path.append("/home")
print (sys.path)
'''
可以看到/home路径已经添加
['D:\\PycharmProjects\\Python\\study2\\day1', 'D:\\PycharmProjects\\Python', 'D:\\python\\Anaconda3\\python37.zip', 'D:\\python\\Anaconda3\\DLLs', 'D:\\python\\Anaconda3\\lib', 'D:\\python\\Anaconda3', 'D:\\python\\Anaconda3\\lib\\site-packages', 'D:\\python\\Anaconda3\\lib\\site-packages\\pymysql-0.9.3-py3.7.egg', 'D:\\python\\Anaconda3\\lib\\site-packages\\win32', 'D:\\python\\Anaconda3\\lib\\site-packages\\win32\\lib', 'D:\\python\\Anaconda3\\lib\\site-packages\\Pythonwin', 'D:\\PyCharm 2018.3.5\\helpers\\pycharm_matplotlib_backend', '/home']
'''

