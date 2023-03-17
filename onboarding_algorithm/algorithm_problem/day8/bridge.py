import sys
input = sys.stdin.readline

def factorial(n):
    f = 1
    for i in range(n):
        f = f * (i+1)

    return f

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(N) * factorial(M-N))))
