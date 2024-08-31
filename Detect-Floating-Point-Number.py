import re
def detect(n):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', n)))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = input()
        detect(n)
    