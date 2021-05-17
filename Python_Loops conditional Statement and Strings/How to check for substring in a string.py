n=input("enter the string")
sub= input('enter the substring that need to be found')
a= n.find(sub)
if a in range(len(n)):
    print(f'the substring "{sub}" is present in the string "{n}"')
else:
    print(f'the substring "{sub}" is not present in the string "{n}"')