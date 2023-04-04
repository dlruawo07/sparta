N = int(input())

stairs = []
max_value = []

for i in range(N):
    stairs.append(int(input()))

max_value.append(stairs[0])
if N >= 2:
    max_value.append(stairs[0]+stairs[1])
    if N > 3:
        max_value.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
        for i in range(3,N):
            max_value.append(max(stairs[i] + stairs[i-1] + max_value[i-3], stairs[i] + max_value[i-2]))
print(max_value[-1])
