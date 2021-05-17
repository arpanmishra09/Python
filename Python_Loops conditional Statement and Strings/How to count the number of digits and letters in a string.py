n = input('enter the word')
i,j,k=0,0,0
for i in range(len(n)):
    if n[i].isdigit():
        j+=1
    elif n[i].isalpha():
        k+=1
print(f'there are {j} digits in : {n}')
print(f'there are {k} letters in : {n}')