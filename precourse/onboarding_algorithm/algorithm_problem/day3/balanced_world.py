import sys

s = ""

open = ['(', '[']
close = [')', ']']

while True:
    s = sys.stdin.readline().rstrip()

    if s == ".":
        break

    stack = []
    is_valid = True

    for ch in s:
        if ch not in open and ch not in close:
            continue
        elif ch in open:
            stack.append(ch)
        elif ch in close:
            if len(stack) == 0:
                is_valid = False
                break
            popped = stack.pop()
            if (popped == '[' and ch == ')') or (popped == '(' and ch == ']'):
                is_valid = False
                break

    if len(stack) != 0:
        is_valid = False
    print('yes' if is_valid is True else 'no')
