with open('text.txt','r') as f, open('textcopy.txt','w') as f1:
    for i in f:
        f1.write(i)

