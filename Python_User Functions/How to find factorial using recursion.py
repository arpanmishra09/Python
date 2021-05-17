def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

x=int(input('enter the required factorial'))

if x<=0:
    print(-1)
elif  x==0:
    print(1)
else:
    ans=fact(x)
    print(ans)
