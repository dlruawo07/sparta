from collections import Counter

N = int(input())

lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort()

avg = round(sum(lst) / N)
med = lst[(N-1)//2]
if N == 1:
    mod = lst[0]
else:
    duplicates = Counter(lst).most_common(2)
    mod = duplicates[1][0] if duplicates[0][1] == duplicates[1][1] else duplicates[0][0]
rng = lst[-1] - lst[0]

print(duplicates)

print(avg, med, mod, rng, sep='\n')