l = int(input('enter the length'))
lst=[]
n=1
i=1
a= {1:'Integer',2:'Float'}
while i<=l:
    try:
        option = int(input('Choose: \n 1: to enter an Integer \n 2: to enter a decimal number\n'))
        value= a.get(option)
        if value=='Integer':
            number = int(input('Enter an Integer '))
            lst.append(number)
        elif value=='Float':
            number = float(input('Enter a decimal number'))
            lst.append(number)

    except:
        print('INVALID INPUT!!'.center(90,'-'))
        print('Kindly note:\n 1. Choose only from the two options given\n 2.Valid inputs are: whole numbers including negative values and decimal numbers ')
        print(f'Attempts left: {4-n}')
        print(''.center(90,'-'))
        n+=1
        if n<4:
            continue
    i+=1