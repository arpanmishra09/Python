n = 'peter piper picked a peck of pickled peppers'
a= n.split()
i=7
while i <= (len(a)+1):
    if i>=0:
        print(a[i],' ',end='')
        i-=1
    else:
        break
