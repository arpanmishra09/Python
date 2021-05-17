lst1 = [item for item in input("Enter the list of keys : ").split()]
lst2 = [int(item) for item in input("Enter the list of items : ").split()]
sum=0
dictionary = dict(zip(lst1,lst2))
print(dictionary)
for i in range(len(dictionary)):
    a = dictionary.get(input('enter the key for the items to be summed'))
    sum+=a


print(sum)