import sys

K = int(sys.stdin.readline())
stack = []

for i in range(K):
    T = int(sys.stdin.readline())
    if T != 0:
        stack.append(T)
    elif T == 0:
        stack.pop()

print(sum(stack))