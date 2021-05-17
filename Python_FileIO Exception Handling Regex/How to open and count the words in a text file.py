with open('text.txt','r') as f:
    for i in f:
        words = i.split()
n=0
for j in words:
    n+=1

print(n)
