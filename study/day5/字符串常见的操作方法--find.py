#字符串常见的操作方法--find/index(索引)
str="my name is it yidaiweiren.txt"

#利用find查找
print (str.find("is"))  #正向查找，即从左到右
'''
8   得到的是is的下标为8
'''

#如果没有该字符串，返回值为-1
print (str.find("cui"))
'''
-1  -1表示没有找到这个值
'''

#反向查找这个值，即从右向左
print (str.rfind("ren"))     #rfind就表示right find 从右向左
'''
22  22表示从右向左查到的以一个字符的索引
'''

#使用index查询
print (str.index("is"))   #正向查找
'''
8   同样得到的结果是8
'''

#使用rindex返乡的查找这个值
print (str.rindex("ren"))
'''
22  同理index也支持反向查询
'''


print ("="*10)
position=str.rfind(".")
print(str[:position])   #打印点以前的所有字符串    #[0:position]这里的数字代表当前位置到最后一位
print(str[position:])   #打印点以及点以后的所有字符串  #[0:position]这里的数字代表当前位置到最后一位
print ("="*10)




#使用index查询，如果没有，返回的是异常
print (str.index("cui"))
'''
  print (str.index("cui"))
ValueError: substring not found     打印异常
'''


