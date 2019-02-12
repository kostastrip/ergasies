L1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=input('dwse xaraktira mexri na dwseis teleia ')
while (x!='.'):
    for i in range(0,25):
        if x==L1[i]:
            L2[i]=L2[i]+1
    x=input('dwse xaraktira mexri na dwseis teleia ')
max=L2[0]
pos=0
for i in range(0,25):
        if L2[i]>max:
            max=L2[i]
            pos=i
min=L2[0]
pos2=0
for i in range(0,25):
        if L2[i]<min:
            min=L2[i]
            pos2=i
print (L2)
print ('o megalyteros einai ',L2[pos])
print ('o mikroteros einai ',L2[pos2])
t=L2[pos]
L2[pos]=L2[pos2]
L2[pos2]=t
print (L2)
print ('o megalyteros einai ',L2[pos2])
print ('o mikroteros einai ',L2[pos])
