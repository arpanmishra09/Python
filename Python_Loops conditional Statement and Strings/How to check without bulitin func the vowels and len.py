def vowel(x): #check vowels in word
    i, j, k = 0, 0, 0
    for i in range(len(x)):
        k+=1
        if x[i]=='a'or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u':
            j+=1
    return(j,k)

n= input('enter 1st the word')
m= input('enter 2nd the word')
a,b=vowel(n)
c,d=vowel(m)

print('the no. of vowels in 1st word:',a)
print('the no. of vowels in 1st word:',c)

#larger word
if b<d:
    print('the larger word is:',m)
else:
    print('the larger word is:',n)