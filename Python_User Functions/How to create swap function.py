def swap(z,y):
    z,y=y,z
    return(z,y)

n1= int(input('1st number:'))
n2= int(input('2nd number'))
a,b=swap(n1,n2)
print(a,b)