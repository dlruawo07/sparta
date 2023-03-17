import sys
input = sys.stdin.readline

N, K = map(int, input().split())

inputs = []

for i in range(N):
    inputs.append(int(input()))

coins = []

for i in range(len(inputs)):
    coins.append(inputs[len(inputs) - 1 - i])

count = 0

for i in coins:
    while i <= K:
        count += 1
        K -= i

    if K == 0:
       break

print(count)