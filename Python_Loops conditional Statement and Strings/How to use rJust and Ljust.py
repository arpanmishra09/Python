n = 'peter piper picked a peck of pickled peppers'
w='peck'
c= n.find(w)
r=c-0
l=len(n)-c
print((''.rjust(r,"*"))+w+(''.ljust(l,"*")))
