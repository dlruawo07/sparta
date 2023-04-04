exps = input().split('-')

result = sum(list(map(int, exps[0].split('+'))))
for i in range(1, len(exps)):
    result -= sum(list(map(int, exps[i].split('+'))))

print(result)