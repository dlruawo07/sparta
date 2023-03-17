T = int(input())

# 0 1 2 3 4 5 6 7
# 0   1 0 1 1 2 3 5 8
# 1   0 1 1 2 3 5 8 13


for i in range(T):
    N = int(input())

    zero = [1, 0]
    one = [0, 1]

    if N == 0:
        print(1, 0)
        continue
    for i in range(2, N+1):
        zero.append(one[-1])
        one.append(one[-2] + one[-1])

    print(zero[-1], one[-1])
