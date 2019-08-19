#字典--items(将字典中的键和值封装成元组)

infor={'name':'laowang','age':18}

#使用items（）方法输出
print (infor.items())
'''
dict_items([('name', 'laowang'), ('age', 18)])  每一个键值对，被封装成为元组，所有元组封装成列表
'''

#使用for循环遍历这个列表，就可以将元组遍历出来，不同于keys（）和values（）方法那样只能遍历一个值

for temp in infor.items():
    print (temp)
'''
('name', 'laowang')
('age', 18)
'''


#延申

for temp in infor.items():
    print ("key=%s,value=%s"%(temp[0],temp[1]))
'''
key=name,value=laowang
key=age,value=18
'''

#延申

for a,b in infor.items():   #a,b操作详见/day8/元组
    print ("key=%s,value=%s"%(a,b))
'''
key=name,value=laowang
key=age,value=18
'''