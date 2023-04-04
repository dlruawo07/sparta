T = int(input())

ans = 0
for i in range(T):
    A, B = map(int, input().split())

    if B % A == 0:
        print(B)
        continue
    elif A % B == 0:
        print(A)
        continue
    
    C = B if B < A else A

    D = 0
    for j in range(2, C+1):

        if A % j == 0 and B % j == 0:
            D = j
    
    if D == 0:
        print(A*B)
        continue
    print(int((A*B) / D))