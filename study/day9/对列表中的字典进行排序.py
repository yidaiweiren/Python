#-*-coding:utf-8-*-
#对列表中的字典进行排序

infors=[{"name":"laowang","age":18},{"name":"boss","age":21},{"name":"xiaoming","age":30}]

#infors.sort(key=lambda x:x['name'])
infors.sort(key=lambda x:x['age'])
#x:x[''],第一个x相当于取了一个字典，第二个“x['']”相当于查抄这个字典下对应的建所对应的值
#print (infors)
print (infors)
'''
按照名字首字母进行排序
[{'name': 'boss', 'age': 21}, {'name': 'laowang', 'age': 18}, {'name': 'xiaoming', 'age': 30}]

按照年龄进行排序
[{'name': 'laowang', 'age': 18}, {'name': 'boss', 'age': 21}, {'name': 'xiaoming', 'age': 30}]
'''