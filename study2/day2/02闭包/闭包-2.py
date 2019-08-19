def test(a,b):
    def test_in(x):
        print (a*x+b)
    return test_in

line1 = test(1,1)
line1(5)       #结果为6


