lst = []
i=0
# iterating till the range
while i == 0 :
    ele = input('enter next number')
    if ele.isdigit():
        lst.append(ele)  # adding the element
    elif '-' in ele:
        b= ele.replace('-', '', 1)
        if b.isdigit():
            lst.append(ele)  # adding the element
        else:
            print('not an integer')
            break
    else:
        print('not an integer')
        break
print(lst)