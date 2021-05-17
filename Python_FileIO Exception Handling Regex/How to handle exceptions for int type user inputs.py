l = int(input('enter the length'))
lst=[]
i=1
while i<=l:
    try:
        number = int(input('Enter an Integer '))
        lst.append(number)
    except:
        print('INVALID INPUT!!'.center(90,'-'))
        print('Kindly note: \nAn integer is a whole number (not a fraction) that can be positive, negative, or zero.')
        print(''.center(90, '-'))
    i+=1

print(lst)