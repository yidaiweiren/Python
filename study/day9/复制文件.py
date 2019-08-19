#复制文件

#获取用户需要复制的文件名
old_file_name=input("请输入要复制的文件名：")

#打开要复制的文件
old_file=open(old_file_name,"r")

#新建一个文件
new_file=open("new_"+old_file_name,"w")     #更多关于文件的拼接详见day5/find用法35-39行

'''
此处发现读取大文件是会耗费很大的内存，决定每次从源文件取1024k，这样系统就不会崩，使用循环实现
#从旧文件种读取数据，并且写入到新文件
content=old_file.read()

#写入到新文件
new_file.write(content)
'''
while True:
    content=old_file.read(1024)     #指定每次读取的文件内容的大小
    if len(content)==0:     #当读取完成时，再继续读取，会读出空字符串，空字符串的len为0，所以这里可以使用if判断
        break
    #写入到新文件
    new_file.write(content)
#关闭两个文件
old_file.close()
new_file.close()