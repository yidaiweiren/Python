#字典--keys（查询字典的键值）

#定义一个字典
infor={'name':'yidaiweiren','age':18}

#len方法打印字典的长度
print (len(infor))
'''
2
'''

#使用keys（）方法取出列表的键值
print (infor.keys())
'''
python2:['name', 'age']     打印为键值，以“列表”形式展现
python3:dict_keys(['name', 'age'])      打印出来为对象，注意查看python版本
'''


#可以使用for遍历去除键名
for temp in infor.keys():
    print (temp)

'''
name
age
'''