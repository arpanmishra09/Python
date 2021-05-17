lst1 = [int(item) for item in input("Enter the list of keys : ").split()]
lst2 = [item for item in input("Enter the list of items : ").split()]
dictionary = dict(zip(lst1,lst2))
print(dictionary)
a= int(input('enter the key to be removed'))
del dictionary[a]
print(dictionary)