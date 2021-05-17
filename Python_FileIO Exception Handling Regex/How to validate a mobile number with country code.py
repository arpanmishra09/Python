### pattern = 'DDD-DDD-DDDD'
import re
numbers = ['+91-991-617-9812','991-617-9812','561-289-674','991-617-981a','+19-9916179812']
for phone in numbers:
    if re.search(pattern = '^\+91-\d{3}-\d{3}-\d{4}$' , string = phone):
        print(phone,' Valid Number')
    else:
        print(phone, ' Invalid Number')
