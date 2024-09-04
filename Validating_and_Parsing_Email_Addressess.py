
import re
import email.utils

n = int(input())

pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'

for i in range(0, n):
    parse_addr = email.utils.parseaddr(input())
    if re.search(pattern, parse_addr[1]):
        print(email.utils.formataddr(parse_addr))