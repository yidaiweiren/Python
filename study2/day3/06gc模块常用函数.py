#gc模块常用函数

import gc

'''
gc.get_threshold():获取gc模块中自动执行垃圾回收的频率
gc.get_count():获取当前自动执行垃圾回收的计数器,返回一个长度为3的列表
gc.set_threshold(threshold1,threshold2,threshold3):设置自动执行垃圾回收的频率
'''
print(gc.get_threshold())

print(gc.get_count())