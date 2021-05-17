def sum(num):
    n = 0
    for i in num:
        n += i
    return n


a= input('enter the numbers').split(' ')
a= list(map(int,a))
result= sum(a)
print(result)