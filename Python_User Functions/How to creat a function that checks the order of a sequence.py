def check(n):
    j = 0
    k = 0
    a = sorted(n)
    d = sorted(n, reverse=True)
    for i in range(len(n)):
        if n[i] == a[j]:
            j += 1
        elif n[i] == d[k]:
            k += 1
        else:
            pass

    if j == len(n):
        print('Ascending order')
    elif k == len(n):
        print('Descending order')
    else:
        print('Random')


try:
    n= (list(map(int,(input('enter the list of numbers').split(' ')))))
    check(n)
except:
    print('Invalid input!')