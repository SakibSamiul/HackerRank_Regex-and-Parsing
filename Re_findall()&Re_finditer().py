import re

s = input()
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

Match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', s, flags=re.I)

if not Match:
    print(-1)
else:
    for i in Match:
        print(i)

# print('\n'.join(match or ['-1']))