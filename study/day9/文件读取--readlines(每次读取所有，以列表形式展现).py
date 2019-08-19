#文件读取--readlines（每次读取所有，以列表的形式展现）

#打开文件
f=open("./Test.py","r")

#读取文件
print (f.readlines())

#关闭文件
f.close()

'''
输出为列表，每一行当成了一个元素
['hello python\n', 'haha\n', 'heihei']
'''