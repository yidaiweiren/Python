#使用pop()方法删除元素
str=['name1','name2','name3','name4']
print (str)
value=str.pop()     #使用pop()方法删除元素
print (str)     #打印删除后的列表
print (value)   #打印删除的元素
str.pop(2)  #使用pop()方法删除第三个元素，利用索引
print (str)