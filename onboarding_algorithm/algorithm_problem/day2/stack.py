import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    T = sys.stdin.readline().split()
    if T[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
    elif T[0] == 'size':
        print(len(stack))
    elif T[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif T[0] == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
    else:
        stack.append(T[1])