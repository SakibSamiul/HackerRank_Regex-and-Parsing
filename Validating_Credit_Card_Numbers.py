
import re
N = int(input())
pattern_1 = r"^[4-6]\d{3}(-?\d{4}){3}$"
pattern_2 = r"(\d)(-?\1){3,}"

no_el = []

def is_valid(credit_card):
    return bool(re.match(pattern_1, credit_card))

def is_invalid(credit_card):
    return re.findall(pattern_2, credit_card)

for i in range(N):
    credit_card = input()
    if is_valid(credit_card) and len(is_invalid(credit_card)) == 0:
        print("Valid")
    else:
        print("Invalid")