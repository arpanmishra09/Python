lst = []
n = int(input("Enter number of elements :"))
for i in range(n):
    ele = int(input('enter the next number'))
    lst.append((ele,ele**2))

print(lst)