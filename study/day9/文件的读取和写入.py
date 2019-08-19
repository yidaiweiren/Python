#文件的读取和写入

#打开文件
f=open("Test.py","r+")    #读取的时候写r，写入的时候写w

#写入文件
f.write("mdfkjbmkl")

#读取文件
print (f.readline())


#关闭写入
f.close()

