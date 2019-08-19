#使用sorted()方法对元素进行零食排序
str=['a1','f1','c2','h5','g7']
print (str)     #打印原始排序
value=sorted(str)      #使用sorted()方法，对元素进行临时排序。可以直接选择排序方式为逆向“reverse=True”
print (value)      #打印临时排序的值
print (str)     #打印初始排序的值

#结果
'''
['a1', 'f1', 'c2', 'h5', 'g7']
['a1', 'c2', 'f1', 'g7', 'h5']
['a1', 'f1', 'c2', 'h5', 'g7']

'''