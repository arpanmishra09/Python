n= ['male','female','male','female','male','female','female','female']
n1= list(map((lambda x: 0 if x=='male' else 1),n))
print(n1)