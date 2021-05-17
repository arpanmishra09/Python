given= (20, 20, 30, 30, 30, 40, 40, 40, 10)
i,a,d,r=0,0,0,0
for j in range(len(given)):
    if given[i]>given[j]:
        d+=1
    elif given[i] < given[j]:
        a+=1

if a>0 and d>0:
    print('random')
elif a>0 and d==0 and r==0:
    print('Ascending order')
else:
    print('descending order')