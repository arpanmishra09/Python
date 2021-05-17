import re
numbers= ['abc@gmail.com','abc@yahoo.com','abc1@gmail.com','Abc@gmail.com','abc@gmail.net']
for n in numbers:
    if re.search('\w@(gmail.com)',n):
        print(f'{n}=Valid')
    else:
        print(f'{n}=invalid')