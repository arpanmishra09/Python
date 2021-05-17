word1= input('enter the 1st word')
word2= set(input('enter the 2nd word'))
print('the common letters are:')
for i in range(len(word1)):
    if word1[i] in word2:
        common = word1[i]
        print(common,end=',')
