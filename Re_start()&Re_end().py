import re
S = input()
k = input()

R = list(re.finditer(r'(?={})'.format(k), S))

if R:
    for i in R:
        print('({0}, {1})'.format(i.start(), i.end() + len(k)-1))
else:
    print('(-1, -1)') 
