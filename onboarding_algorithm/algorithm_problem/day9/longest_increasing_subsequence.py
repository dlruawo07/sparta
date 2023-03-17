N = int(input())

A = list(map(int, input().split()))[:N]
B = [0]

for i in range(N):
    if A[i] > B[-1]:
        B.append(A[i])
    else:
        for j in range(len(B)):
            if B[j] >= A[i]:
                B[j] = A[i]
                break

print(len(B)-1)