n = int(input())

triangle = []

triangle.append(list(map(int, input().split())))

if n >= 2:
    triangle.append(list(map(int, input().split())))
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

    for i in range(2, n):
        triangle.append(list(map(int, input().split())))
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


print(max(triangle[-1]))


n = int(input())

prev = [-1] * n
curr = [-1] * n

curr = list(map(int, input().split()))
if n >= 2:
    prev = curr
    curr = list(map(int, input().split()))
    curr[0] += prev[0]
    curr[1] += prev[0]

    for i in range(2, n):
        prev = curr
        curr = list(map(int, input().split()))
        for j in range(i+1):
            if j == 0:
                curr[j] += prev[0]
            elif j == i:
                curr[j] += prev[i-1]
            else:
                curr[j] += max(prev[j-1], prev[j])

print(max(curr))
