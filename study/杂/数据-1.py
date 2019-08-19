#-*-coding:utf-8-*-
import matplotlib.pyplot as plt

a = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]

#设置线条粗细
plt.plot(a,linewidth=5)

#设置图标标题
plt.title("A Number",fontsize=20)

#设置坐标轴标签
plt.xlabel("Value",fontsize=14)
plt.ylabel("A_Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

#显示图片
plt.show()

