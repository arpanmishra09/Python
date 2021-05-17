def fact(x):
    j=1
    i=1
    while i<=x:
        j=j*i
        i+=1
    return j

x=int(input('enter the required factorial'))

if x<=0:
    print(-1)
elif  x==0:
    print(1)
else:
    ans=fact(x)
    print(ans)