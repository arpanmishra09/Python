n=int(input('enter the number within 0 to 9'))
if n < 10:
    d= {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    print (d.get(n))
else:
    print('the number entered is outside range')
