#批量重命名文件夹中的文件名

import os

#获取用户要重命名文件的文件夹名
folder_name=input("请输入需要命名文件的父文件夹：")

#获取文件夹中的所有文件名
file_names=os.listdir(folder_name)

#改变路径，进入此文件夹下
os.chdir(folder_name)

#重命名

for name in file_names:
    new_name=os.rename(name,"[一代伟人]-"+name)
    print (new_name)

'''
BUG：未解决删除拼接的字符
for name in file_names:
    position=name.rfind("-")
    old_names=name[position:]    #[0:position]这里的数字代表当前位置到第一位
    #replace_names=name.replace(old_names,'')    #字符串的替换

    print (old_names)
'''
