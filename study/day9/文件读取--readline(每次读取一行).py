#文件读取--readline(每次只读一行)

#打开文件
f=open("Test.py","r")

#读取文件
print (f.readline())

#关闭文件
f.close()