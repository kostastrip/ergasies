def plus(k,l):
    return k+l
def times(k,l):
    return k*l
def minus(k,l):
    return k-l

pr=input("ti praksi thes na kaneis? ")
a=input('Dwse ton prwto ari8mo ')
b=input('Dwse ton deytero ari8mo ')
if a=='one':
    a1=1
elif a=='two':
    a1=2
elif a=='three':
    a1=3
elif a=='four':
    a1=4
elif a=='five':
    a1=5
elif a=='six':
    a1=6
elif a=='seven':
    a1=7
elif a=='eight':
    a1=8
elif a=='nine':
    a1=9
elif a=='zero':
    a1=0
if b=='one':
    a2=1
elif b=='two':
    a2=2
elif b=='three':
    a2=3
elif b=='four':
    a2=4
elif b=='five':
    a2=5
elif b=='six':
    a2=6
elif b=='seven':
    a2=7
elif b=='eight':
    a2=8
elif b=='nine':
    a2=9
elif b=='zero':
    a2=0
if(pr=='plus'):
    x=plus(a1,a2)
    print (x)
elif(pr=='times'):
    x=times(a1,a2)
    print (x)
elif(pr=='minus'):
    x=minus(a1,a2)
    print (x); 
