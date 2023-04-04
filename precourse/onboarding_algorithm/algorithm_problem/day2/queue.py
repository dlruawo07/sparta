import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])

for i in range(N):
    T = sys.stdin.readline().split()
    if T[0] == 'pop':
        print(-1 if len(queue) == 0 else queue.popleft())
    elif T[0] == 'size':
        print(len(queue))
    elif T[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif T[0] == 'back':
        print(queue[-1] if len(queue) != 0 else -1)
    elif T[0] == 'front':
        print(queue[0] if len(queue) != 0 else -1)
    else:
        queue.append(T[1])