#-*-coding:utf-8-*-
#对字典进行排序

#引入
infors=[11,21,35435,4,656,5,344,55]
infors.sort()
print (infors)
'''
[4, 5, 11, 21, 55, 344, 656, 35435]
'''

nums=[1,34,566,2244,111,123]
nums.sort(reverse=True)
print (nums)
'''
[2244, 566, 123, 111, 34, 1]    反向排序
'''

nums.reverse()
print (nums)
'''
[1, 34, 111, 123, 566, 2244]    倒叙，前后位置颠倒互换
'''
#=============================================================================