import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
count = 0

deque = deque(range(1, N+1))

input = list(map(int, sys.stdin.readline().split()[:M]))

for n in input:
    i = deque.index(n)
    if i < len(deque) / 2 and i != 0:
        deque.rotate(-i)
        count += i
    elif i >= len(deque) / 2 and i != 0:
        deque.rotate(len(deque) - i)
        count += len(deque) - i

    deque.popleft()

print(count)
