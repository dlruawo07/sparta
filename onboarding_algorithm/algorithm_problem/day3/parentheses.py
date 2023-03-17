import sys

T = int(sys.stdin.readline())

for i in range(T):
    a = sys.stdin.readline().rstrip()

    is_valid = True
    stack = []

    if a[0] == ')' or a[-1] == '(':
        is_valid = False
    else:
        for c in a:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    is_valid = False
                    break
                stack.pop()
        if len(stack) != 0:
            is_valid = False
    print('YES' if is_valid is True else 'NO')
