#定位读写
#seek(移动的量/偏移量（比如移动2个字节），0文件开头_1文件中间_2文件末尾)
#文件读取种每读取一个字符，指针会往后移动一位，读取完成不会自动回到文件开头，最后没有内容就是空字符串，所以可以使用seek(0,0)将指针拉回文件开头
#tell()方法：获取当前指针所处的位置

#打开文件
f=open("./Test.py","r")

#定位读写
f.seek(2,0)     #从开头、从第三个字符开始读取（跳过前两个）
print (f.tell())    #结果为2，当前指针在第一行第三个字符（字符从0开始）

#读取文件
print (f.read())

#将指针拉回文件开头
f.seek(0,0)
print (f.tell())    #结果为0，当前指针在第一行第一个字符

#再次读取文件
print (f.read())

#关闭文件
f.close()



'''
llo python      没有前两个字符
haha
heihei
'''

'''
hello python    指针拉回的结果，读取所有。不拉回指针读取为空
haha
heihei
'''