import sys

def get_dist_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    d = get_dist_between_points(x1, y1, x2, y2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    # 1. 서로의 외부에 위치, 혹은 한 원이 다른 원의 내부에 위치
    elif r1 + r2 < d or (abs(r1 - r2) > d and r1 != r2):
        print(0)
    
    # 2. 외접 혹은 내접
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    
    # 3. 서로 다른 두 점에서 만남
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)
    
    else:
        print(-1)