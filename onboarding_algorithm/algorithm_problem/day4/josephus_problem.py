import sys
from collections import deque

# N: number of people (1~N)
# K: every [K]th person is eliminated

# there are N people in deque
# 1. rotate left K-1 times (until K is at 0th index)
# 2. popleft, append that to sequence
# 3. repeat 1 and 2 until deque is empty
# 4. if deque is empty, print the result in a given format

N, K = map(int, sys.stdin.readline().split())

sequence = []
deque = deque(range(1, N+1))

while len(deque) != 0:
    deque.rotate(-(K-1))
    sequence.append(deque.popleft())

print('<', end="")
for i in range(0, len(sequence) - 1):
    print(sequence[i], ', ', sep="", end="")
print(sequence[-1], '>', sep="")
