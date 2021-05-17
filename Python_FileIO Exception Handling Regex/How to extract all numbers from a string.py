import re
stri= 'adbv345hj43hvb42'
print('The digits in the string are as follows:')
for i in stri:
    if re.match(pattern='\d',string=i):
        print(i,end=' ')
