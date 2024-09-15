

import re
s = ''

for _ in range(int(input())):
    s += input() + '\n'

s = re.sub(r'(?<=\s)&&(?=\s)','and',s)
s = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', s)

print(s)