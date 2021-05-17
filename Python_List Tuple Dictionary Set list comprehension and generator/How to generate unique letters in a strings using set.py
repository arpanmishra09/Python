word1= (input('enter the 1st word'))
word2= (input('enter the 2nd word'))
combined= word1.join(word2)
print(f'the uncommon letters are: {set(combined)}')