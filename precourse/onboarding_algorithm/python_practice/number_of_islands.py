from collections import deque

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]

def island_dfs_stack(grid):
    # dx, dy: 상하좌우의 인덱스
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # grid의 길이와 높이
    rows, cols = len(grid), len(grid[0])
    # 섬의 개수
    count = 0
    for row in range(rows):
        for col in range(cols):
            # 각 요소를 순회하며 1이 아닐 때는 다음 col로 넘어감
            if grid[row][col] != "1":
                continue

            # 1이라면 무조건 섬의 개수 증가
            count += 1
            # 해당 인덱스를 stack에 저장
            stack = [(row, col)]

            while stack:
                # 가장 최근에 삽입된 인덱스짝 pop
                x, y = stack.pop()
                # 해당 인덱스를 0으로 수정
                grid[x][y] = "0"
                # 상,하,좌,우 총 4개의 위치 확인
                for i in range(4):
                    # nx, ny 상하좌우의 인덱스짝
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # nx나 ny가 범위 밖이거나 해당 인덱스의 값이 1이 아니면 다음 i로 넘어감
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != "1":
                        continue
                    # nx, ny를 stack (grid[nx][ny]는 1임)
                    stack.append((nx, ny))

    return count

def island_dfs_recursive(grid):
    # dx, dy: 상하좌우의 인덱스
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    count = 0

    def dfs_recursive(r, c):
        # 재귀의 종료 조건: r과 c가 grid의 범위를 벗어나거나 해당 인덱스의 값이 1이 아닌 경우
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
            return
        # 해당 인덱스의 값을 0으로 바꿈
        grid[r][c] = "0"

        # 현재 인덱스의 상,하,좌,우 인덱스들에 대해 재귀 실행
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return
    
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                continue

            count += 1
            dfs_recursive(r, c)

    return count

def island_bfs_queue(grid):
    # dx, dy: 상하좌우의 인덱스
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # grid의 길이와 높이
    rows, cols = len(grid), len(grid[0])
    # 섬의 개수
    count = 0
    for row in range(rows):
        for col in range(cols):
            # 각 요소를 순회하며 1이 아닐 때는 다음 col로 넘어감
            if grid[row][col] != "1":
                continue

            # 1이라면 무조건 섬의 개수 증가
            count += 1
            # 해당 인덱스를 stack에 저장
            q = deque([(row, col)])

            while q:
                # 맨 처음에 삽입된 인덱스짝 pop
                x, y = q.popleft()
                # 해당 인덱스를 0으로 수정
                grid[x][y] = "0"
                # 상,하,좌,우 총 4개의 위치 확인
                for i in range(4):
                    # nx, ny 상하좌우의 인덱스짝
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # nx나 ny가 범위 밖이거나 해당 인덱스의 값이 1이 아니면 다음 i로 넘어감
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != "1":
                        continue
                    # nx, ny를 q (grid[nx][ny]는 1임)
                    q.append((nx, ny))

    return count