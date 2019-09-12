def test(a,b):
    print('---1---')
    def test_in(x):
        print (a*x+b)
    print('---2---')
    return test_in

line1 = test(1,1)
line1(5)       #结果为6


