#-*-coding:utf-8-*-
#列表当作全局变量
#列表或字典当作全局变量是，可以直接在函数中使用

nums=[11,22,33]

def nums_append():
    nums.append(44)

def print_nums():
    print (nums)

nums_append()
print_nums()
'''
[11, 22, 33, 44]    成功添加
'''

infors={"name":"laowang"}

def infors_append():
    infors['age']=18       #往字典中添加内容 键-》值
    #print (infors)

def print_infors():
    print (infors)

infors_append()
print_infors()