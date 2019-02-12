def sumIntervals(L):
    sum=L[1]-L[0]
    x=2
    while x<len(L):
        f=0
        for i in range(0,x,1):
            if L[x]<L[i]:
                f=1
        if f==0:
            sum=sum+L[x+1]-L[x]
        else:
            i=1
            while i<=x:
                if L[x+1]>L[i]:
                    sum=sum+L[x+1]-L[i]
                    break
                i=i+2
        x=x+2
    return sum
   

L=[]
x=int(input('dwse times '))
while x!=10000:
    L.append(x)
    x=int(input('dwse times mexri to 10000 '))
print (L)
x= sumIntervals(L)
print (x)


