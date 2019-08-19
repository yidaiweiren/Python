'''
闭包：在函数内部定义了一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的变量称之为“闭包”。
'''
'''
执行流程
    1.执行ret = test(100),先处理等号右边
        打印-----1-----
    2.走到test_in没有执行
    3.执行test中的第二个print
        打印-----3-----
    4.return到test_in
    5.执行test_in,将得到的结果返回给test，test又将结果给变量ret，因为ret=test（），所以就ret = test_in()
    6.打印一条横线
    7.ret(2)也就等于test_in(2)
'''
def test(number):
    print ("-----1-----")
    print(number)

    def test_in(number2):
        print ("-----2-----")
        print (number+number2)

    print ("-----3-----")
    return test_in


ret = test(100)
print ("+="*25)
ret(2)