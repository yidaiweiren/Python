'''
多线程拷贝文件
'''
import os
from multiprocessing import Pool,Manager

#定义拷贝文件方法
def copyFileTask(name,oldFolderName,newFloderName,queue):
	'''完成拷贝一个文件的功能'''
	#print(name)
	fr = open(oldFolderName+"/"+name)	#只读打开old文件
	fw = open(newFloderName+"/"+name,"w")	#只写的方式打开新文件
	#print("-----")

	content = fr.read()	#一次性读取源文件所有内容
	fw.write(content)	#将读取的文件，写入新的文件中

	fr.close()
	fw.close()

	queue.put(name)	#执行完一个文件，将文件名扔进队列中，下面由主进程统计


def main():
	#0.获取需要拷贝的文件夹的名字
	oldFolderName = input("请输入需要拷贝的文件夹名：")


	#1.创建一个新文件夹
	newFloderName = oldFolderName+"-副件"
	#print(newFloderName)
	os.mkdir(newFloderName)

	#2.获取old文件夹中所有文件的名字
	fileNames = os.listdir(oldFolderName)
	#print(fileNames)


	#3.使用多进程的方式拷贝old文件夹中的所有文件到新文件夹中
	pool = Pool(5)	#创建5个进程同时拷贝
	queue = Manager().Queue()

	for name in fileNames:
		pool.apply_async(copyFileTask,args=(name,oldFolderName,newFloderName,queue))

	#pool.close()
	#pool.join()

	num = 0
	allNum = len(fileNames)
	while True:
		queue.get()
		num+=1
		copyRight = num/allNum
		print("\r拷贝文件的进度是：%.2f%%"%(copyRight*100),end="")	#%要写两个%%

		#停止程序
		if num==allNum:
			break


	print("\n已完成所有文件的拷贝！！！！！")

if __name__ == "__main__":
	main()