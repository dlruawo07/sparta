N, K = map(int, input().split())

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
items = [[0, 0]]

for i in range(N):
    items.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W = items[i][0]
        V = items[i][1]

        if j >= W:
            knapsack[i][j] = max(V + knapsack[i - 1][j - W], knapsack[i - 1][j])
        else:
            knapsack[i][j] = knapsack[i - 1][j]

print(knapsack[N][K])

# i\j  0   1   2   3   4   5    6    7
#  0  [0] [0] [0] [0] [0] [0]  [0]  [0]
#  1  [0] [0] [0] [0] [0] [0]  [13] [13]
#  2  [0] [0] [0] [0] [8] [8]  [13] [13]
#  3  [0] [0] [0] [6] [8] [8]  [13] [0]      (6+8, 13)
#  4  [0] [0] [0] [6] [8] [12] [13] [13]

# for i in range(N+1):
#     for j in range(K+1):
#         print("[", end="")
#         print(knapsack[i][j], "]", sep="", end="")
#     print()

# W들을 리스트에 따로 추가 / 정렬
# 2

# 알고리즘
# 1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.

# 2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.

# 3-0) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.

# 3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.

# 3-2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.

# 4) 3-1과 3-2 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.

# 5) knapsack[N][K]는 곧, K무게일 때의 최댓값을 가리킨다.

# W/V  | 0 1 2 3 4  5  6  7
# 6/13 | 0 0 0 0 0  0 13 13 
# 4/8  | 0 0 0 0 8  8 13 13
# 3/6  | 0 0 0 6 8  8 13 14 (이전 물건 중 4kg인 것 +)
# 5/12 | 0 0 0 6 8 12 13 14

# sack[i][j] = max(현재 물건의 가치 + sack[이전 물건][현재 가방 무게 - 현재 물건 무게], sack[이전 물건][현재 가방 무게])
# sack[i][j] = max(value + sack[i - 1][j - weight], sack[i - 1][j])

# N = 5
# K = 5
#     0 1 2 3 4 5
# 1/2 0 2 2 2 2 2
# 2/3 0 2 3 3 3 5
# 3/4 0 2 3 4 4 7
# 4/5 0 2 3 4 5 7
# 5/1 0 2 3 4 5 7