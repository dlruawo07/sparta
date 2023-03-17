import sys

a = int(sys.stdin.readline())
stack = []
top = 0
max = -1
s = ""

for i in range(a):
    n = int(sys.stdin.readline())

    if n > top:
        stack.extend(range(max+1 if max != -1 else max+2, n))
        s += '+\n' * (n - (max+1 if max == -1 else max)) + '-\n'

    elif n == top:
        stack.pop()
        s += '-\n'
    else:
        s = 'NO'
        break

    max = n if n > max else max
    top = stack[-1] if len(stack) != 0 else 0

print(s)
