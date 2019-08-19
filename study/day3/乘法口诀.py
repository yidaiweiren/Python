#乘法口诀
for i in range (1,10):
    for j in  range (1,10):
        num=i*j
        print (str(i)+'*'+str(j)+'='+str(num),end=' ')
        if j>i-1:
            break
    print ()
print ("#"*70)
for m in range(9,0,-1):
    for n in range (9,0,-1):
        sum=m*n
        print (str(m)+'*'+str(n)+'='+str(sum),end=" ")
        if n<m:
            break
    print ()
#i=3
#j=1 1>3-1  flase
# j=2 2>3-1 flase
# j=3 3>3-1 true
#j>3-1

#m=1 n=1 1*1=1
#m=1 n=2 1*2=2
#m<n