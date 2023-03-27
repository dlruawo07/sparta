N = int(input())

def hanoi(n, start, end):
    if n == 0: return
    hanoi(n-1, start, 6 - start - end)
    print(start, end)
    hanoi(n-1, 6 - start - end, end)

print(2 ** N - 1)
hanoi(N, 1, 3)

##

# 1. 작은 원반 n-1개를 'A'에서 'B'로 이동
# 2. 큰 원반 1개를 'A'에서 'C'로 이동
# 3. 작은 원반 n-1개를 'B'에서 'C'로 이동 