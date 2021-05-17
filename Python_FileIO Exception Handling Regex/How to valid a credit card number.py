import re
card = input('enter the card number to be checked\n')
if 13<=len(card)<=16:
    if re.search(pattern='^4\d{12}',string=card) or re.search(pattern='^4\d{13}',string=card) or \
            re.search(pattern='^4\d{14}',string=card) or re.search(pattern='^4\d{15}',string=card):
        print(f'{card} is a valid VISA card')
    elif re.search(pattern='^5\d{12}',string=card) or re.search(pattern='^5\d{13}',string=card) or \
            re.search(pattern='^5\d{14}',string=card) or re.search(pattern='^5\d{15}',string=card):
        print(f'{card} is a valid Master Card')
    elif re.search(pattern='^37\d{11}',string=card) or re.search(pattern='^37\d{12}',string=card) or \
            re.search(pattern='^37\d{13}',string=card) or re.search(pattern='^37\d{14}',string=card):
        print(f'{card} is a valid American Express card')
    elif re.search(pattern='^6\d{12}',string=card) or re.search(pattern='^6\d{13}',string=card) or \
            re.search(pattern='^6\d{14}',string=card) or re.search(pattern='^6\d{15}',string=card):
        print(f'{card} is a valid Discover card')
    else:
        print(f'{card} is not a valid Credit Card')