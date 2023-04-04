def factorial(n):
    f = 1
    for i in range(n):
        f = f * (i+1)

    return f


N, K = map(int, input().split())

print(int(factorial(N) / (factorial(K) * factorial(N-K))))
