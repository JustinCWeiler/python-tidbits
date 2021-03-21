import sys

def shift(c, i):
    if c.isupper():
        return chr((ord(c) - ord('A') + i) % 26 + ord('A'))
    else:
        return chr((ord(c) - ord('a') + i) % 26 + ord('a'))


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


inp = ' '.join(sys.argv[1:])

g = fib()
s = ''
for c in inp:
    s += shift(c, next(g)) if c.isalpha() else c

print(s)