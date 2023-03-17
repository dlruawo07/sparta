import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0 and heap:
        print((-1) * heapq.heappop(heap)) # 최소 힙의 최소값을 양수로 만들어 출력
    elif x == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, (-1) * x) # 기존 heapq는 최소 힙만 지원하기 때문에 삽입하려는 숫자를 음수로 만들어 삽입
    