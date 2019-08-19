#字符串切片
str="abcdefghij"

#取出2-5位的字符 结果位cde，但是发现cde对应是【2，3，4】没有取到5
#所以每次要在要取的值界限的后面+1
print (str[2:5])
print (str[2:6])
'''
cde
cdef
'''

#从第2个字符取到倒数第二个字符
print (str[1:-2])
print (str[1:-1])
'''
bcdefgh
bcdefghi
'''

#从第3个字符取到最后
print (str[2:])
'''
cdefghij
'''

#从第3个字符取到最后，但是每隔一个取一下
#步长：每一次走的长度 [起始：结束：步长]
#步长位1，默认可以省略
print (str[2::1])
print (str[2::2])
'''
cdefghij
cegi
'''

#倒序，让所有字串倒着输出
print (str[-1:])
#[-1:0]取不出来，因为步长是1，往右边走，右边没有字符，所以取不出来
print (str[-1:0])
#[-1：0：-1]没有第一个字符，因为界限是0，所以得去取0的左边，也就是空
print (str[-1:0:-1])
print (str[-1::-1])
print (str[::-1])   #步长-1直接倒序
print (str[::1])    #步长为1正序
'''
j

jihgfedcb
jihgfedcba
jihgfedcba
abcdefghij
'''