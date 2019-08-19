#字典--values（查询字典的键值对应的值）

#定义一个字典
infor={'name':'yidaiweiren','age':18}

#使用values（）方法打印键值对应的值
print (infor.values())
'''
python2:['yidaiweiren', 18]     打印的值以列表形式展现
python3:dict_values(['yidaiweiren', 18])       打印的结果以对象形式展现
'''

#可以使用for循环遍历出key对应的value
for temp in infor.values():
    print (temp)
'''
yidaiweiren
18
'''