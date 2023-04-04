from BinaryMaxHeap import BinaryMaxHeap
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
k = int(input())

max_heap = BinaryMaxHeap()

for i in nums:
    max_heap.insert(i)

# for i in range(k):
#     out = max_heap.extract()

# print(out)
# list에 extract를 k번 한 값들의 list의 k-1번째 요소 저장
print([max_heap.extract() for _ in range(k)][k - 1])