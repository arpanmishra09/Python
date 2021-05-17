lst = []
even=[]
odd=[]
n = int(input("Enter number of elements :"))
j= n
for i in range(n):
    ele = int(input('enter the next number'))
    lst.append(ele)

even= list(i for i in lst if i%2==0)
odd= list(i for i in lst if i%2!=0)
print(f'even:{even}\nodd:{odd}')
