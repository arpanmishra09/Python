l = int(input('enter the length'))
lst=[]
n=1
i=1
a= {1:'Integer',2:'Float'}
while i<=l:
    try:
        option = int(input('Choose: \n 1: To enter an integer \n 2: To enter a decimal number\n'))
        value= a.get(option)
        if value=='Integer':
            number = int(input('Enter an Integer:'))
            lst.append(number)
        elif value=='Float':
            number = float(input('Enter a Decimal number:'))
            lst.append(number)

    except:
        print('INVALID INPUT!!'.center(90,'-'))
        print('Kindly note:\n 1. Choose only from the two options given\n 2.Valid inputs are: whole numbers including negative values and decimal numbers ')
        print(''.center(90,'-'))
        print(f'ATTEMPTS LEFT: {4 - n}')
        print(''.center(90, '-'))
        n+=1
        if n<4:
            continue
    i+=1

print(lst)