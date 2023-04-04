a, b = map(int, input().split())

if b % a == 0:
    print(a, b, sep='\n')
elif a % b == 0:
    print(b, a, sep='\n')
else:
    c = b if b < a else a
    d = 1
    for j in range(2, c+1):
        if a % j == 0 and b % j == 0:
            d = j

    print(d, (a*b) // d, sep='\n')