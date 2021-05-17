def fact(x):
    j=1
    for i in range(1,x+1):
        j=j*i
    return j

x=int(input('enter the required factorial'))

if x<=0:
    print(-1)
elif  x==0:
    print(1)
else:
    ans=fact(x)
    print(ans)

