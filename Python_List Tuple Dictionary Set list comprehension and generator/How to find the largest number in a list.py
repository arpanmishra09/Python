lst = []
n = int(input("Enter number of elements :"))
j= n
for i in range(n):
    ele = float(input('enter the next number'))
    lst.append(ele)

print(f'{max(lst)} is the max number' )