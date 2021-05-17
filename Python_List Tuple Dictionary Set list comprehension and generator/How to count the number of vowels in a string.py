vowels = set('aeiou')
word= input('enter the word')
n=0
for i in range(len(word)):
    if word[i] in vowels:
        n+=1


print(f'the number of vowels present in {word} is {n}')
