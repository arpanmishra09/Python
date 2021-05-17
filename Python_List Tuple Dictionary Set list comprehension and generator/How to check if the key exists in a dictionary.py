lst1 = [int(item) for item in input("Enter the list of keys : ").split()]
lst2 = [item for item in input("Enter the list of items : ").split()]
dictionary = dict(zip(lst1,lst2))
print(dictionary)
a= dictionary.get(int(input()))
if a is None:
    print(' key not found')
else:
    print('key found')