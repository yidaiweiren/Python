import pdb
def getAverage(a,b,c):
    result = c
    print("result=%d"%result)
    return result


a = 100
b = 100
c = a+b

ret = getAverage(a,b,c)

pdb.set_trace()

print(ret)