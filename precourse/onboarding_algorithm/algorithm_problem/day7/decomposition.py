N = int(input())
ans = 0

for num in range(N-1, 0, -1):
    sum = 0
    tmp = num
    for j in range(len(str(num))):
        sum += tmp % 10
        tmp /= 10
    if num + sum == N:
        ans = num

print(ans)
