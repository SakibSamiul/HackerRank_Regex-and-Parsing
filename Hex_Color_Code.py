import re

pattern = r"#[0-9a-fA-F]{3,6}(?=[;),])"
n = int(input())
res = []


for _ in range(n):
    res += re.findall(pattern, input().strip())
    
print(*res, sep='\n')