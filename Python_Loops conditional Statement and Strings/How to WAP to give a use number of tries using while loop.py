lst = []
i=0
n=0
print('enter any alphabet 4 times to exit')
while n<=3 :
    ele = input('enter next number')
    if not ele.isalpha():
        lst.append(ele)
    elif ele == " ":
        print('not a number try again')
        n+=1
    else:
        print('not a number try again')
        n += 1
print(lst)