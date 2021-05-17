lst = []
n = int(input("Enter number of elements :"))
for i in range(n):
    ele = input('enter the next word')
    lst.append(ele)

longest_word = ''
for word in lst:
    if len(word) > len(longest_word):
        longest_word = word
print(f'the length of the longest word "{longest_word}" is: {len(longest_word)}')