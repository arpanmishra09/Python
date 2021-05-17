def find_type(var):
    if var.isdigit() and '-' in var and '.' not in var:
        print(f'{var} is integer')
    elif '.' in var and '-' in var and var[0] !='(' and var[0] !='{' and var[0] !='[':
        print(f'{var} is Float Type')
    elif var == 'True' or var == 'False' :
        print(f'{var} is Bool Type')
    elif var[0]== '[' and var[-1]==']':
        print(f'{var} is list type')
    elif var[0]== '(' and var[-1]==')':
        print(f'{var} is tuple type')
    elif var[0]== '{' and var[-1]=='}':
        print(f'{var} is list type')
    elif var[0]== '{' and var[-1]=='}' and ':' in var:
        print(f'{var} is dictionary type')
    else:
        print(f'{var} is string type')




find_type(input('enter the input'))