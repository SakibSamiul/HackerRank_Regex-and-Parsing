
import re
n = int(input())
for i in range(n):
    i = str(input())
    if (bool(re.search(r'^[789](\d{9})$', i))):
        print("YES")
    else:
        print("NO")
