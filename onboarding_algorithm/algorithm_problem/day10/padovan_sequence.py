T = int(input())
dp = [1, 1, 1, 2, 2] + [0] * 95

for i in range(T):
    n = int(input())
    for j in range(5, n):
        dp[j] = dp[j-5] + dp[j-1]

    print(dp[n-1])