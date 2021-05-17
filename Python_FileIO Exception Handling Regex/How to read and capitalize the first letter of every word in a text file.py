with open('text.txt','r') as f:
    for i in f:
        words = i.split()
cap= [j.capitalize() for j in words]
print(cap)