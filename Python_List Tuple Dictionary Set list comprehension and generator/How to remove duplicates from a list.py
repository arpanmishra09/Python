lst = []
n = int(input("Enter number of elements :"))
j= n
for i in range(n):
    ele = input('enter the next item')
    lst.append(ele)

no_duplicates= set(lst)
print(no_duplicates)