num1=float(input('enter the larger number'))
num2=float(input('enter the smaller number'))
option= int(input(' choose one of  the sl nos. for operation: \n1.To add\n2. to subtract\n3. To multiply'
                  '\n4. To divide\n5. To divide and find quotient\n6. To divide and find remainder'
                  '\n7. To find num1 to the power of num2\n8. To Come out of the program\nchoose an option:'))

if num1<num2 and option <= 8:
    n1,n2=num2,num1

    d = {1: (n1 + n2), 2: (n1 - n2), 3: (n1 * n2), 4: (n1 / n2), 5: (n1 // n2), 6: (n1 % n2), 7: (n1 ** n2),8: "thank you"}
    print(d.get(option))
elif num1 == num2 or num1>num2 and option <=8:
    n1,n2=num1,num2
    d = {1:(n1+n2),2:(n1-n2),3:(n1*n2),4:(n1/n2),5:(n1//n2),6:(n1 % n2),7:(n1 ** n2),8: "thank you"}
    print(d.get(option))

else:
    print('ERROR: wrong option')

