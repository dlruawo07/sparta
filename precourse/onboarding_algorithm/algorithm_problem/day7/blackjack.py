# N, M = map(int, input().split())

# lst = list(map(int, input().split()))
# ans = []

# for i in range(0, len(lst)-2):
#     for j in range(i + 1, len(lst)-1):
#         for k in range(j + 1, len(lst)):
#             ans.append(lst[i] + lst[j] + lst[k])

# max = 0
# ans.sort()
# for i in range(len(ans)):
#     if ans[i] > M:
#         max = ans[i-1]
#         break
# print(max if max != 0 else ans[len(ans) - 1])

N, M = map(int, input().split())

lst = list(map(int, input().split()))
max = 0

for i in range(0, len(lst)-2):
    for j in range(i + 1, len(lst)-1):
        for k in range(j + 1, len(lst)):
            tmp = lst[i] + lst[j] + lst[k]
            if tmp <= M and tmp > max:
                max = tmp

print(max)