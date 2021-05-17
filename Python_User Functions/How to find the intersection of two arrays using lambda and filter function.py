lis1=(input('enter the 1st set of numbers')).split(' ')
lis2=(input('enter the 2nd set of numbers')).split(' ')
n= list(filter((lambda x: x in lis1),lis2))
print(set(n))