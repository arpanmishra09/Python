def add():
    try:
        num= (list(map(float,input('enter the numbers').split(' '))))
    except:
        print('ERROR'.center(90,'-'))
        print('INVALID INPUT'.center(90))
        print('ERROR'.center(90,'-'))
    else:
        n = num[0]
        for i in num[1:]:
            n = n + i
        print(f'answer= {n}')

def subs():
    try:
        num = (list(map(float, input('enter the numbers').split(' '))))
    except:
        print('ERROR'.center(90, '-'))
        print('INVALID INPUT'.center(90))
        print('ERROR'.center(90, '-'))
    else:
        n=num[0]
        for i in num[1:]:
                n= n-i
        print(f'answer= {n}')

def mul():
    try:
        num = (list(map(float, input('enter the numbers').split(' '))))
    except:
        print('ERROR'.center(90, '-'))
        print('INVALID INPUT'.center(90))
        print('ERROR'.center(90, '-'))
    else:
        n = num[0]
        for i in num[1:]:
            n = n*i
        print(f'answer= {n}')

def div():
    try:
        num = (list(map(float, input('enter the numbers').split(' '))))
    except:
        print('ERROR'.center(90, '-'))
        print('INVALID INPUT'.center(90))
        print('ERROR'.center(90, '-'))
    else:
        n=num[0]
        for i in num[1:]:
                n= n/i
    print(f'answer= {n}')

option= int(input('enter:\n1:addition\n2:subtraction\n3:multiplication\n4:division\n5:exit\n'))

if option==1:
    add()
elif option==2:
    subs()
elif option==3:
    mul()
elif option==4:
    div()
else:
    print('Thank You')




