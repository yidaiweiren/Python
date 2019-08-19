#组织列表
#使用sort()方法对列表进行永久排序
#都是小写，按学号字母顺序排序
#使用reverse=True参数来将字母进行“反向”排序
#True首字母必须大写
str=['a1','f1','c2','h5','g7']
print (str)
str.sort()  #使用sort()方法对元素进行永久排序
print (str)
str.sort(reverse=True)  #加入反向参数 从小到大排序
print (str)
#结果
'''
['a1', 'f1', 'c2', 'h5', 'g7']
['a1', 'c2', 'f1', 'g7', 'h5']
['h5', 'g7', 'f1', 'c2', 'a1']

'''