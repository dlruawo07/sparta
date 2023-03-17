# if positive number A must be a real divisor of positive number N
# N must be a multiple of A, and A must not be neither 1 nor N
# given all divisors of some N, get N

# N: number of divisors
# divisors: all divisors of N

# method 1 (max(list), min(list))
import sys

N = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))

print(max(divisors) * min(divisors))

# method 2 (max_heap and min_heap)
# import sys, heapq

# N = int(sys.stdin.readline())
# divisors = list(map(int, sys.stdin.readline().split()))

# min_heap = []
# max_heap = []

# for i in divisors:
#     heapq.heappush(min_heap, i)
#     heapq.heappush(max_heap, i * -1)

# print(heapq.heappop(min_heap) * (heapq.heappop(max_heap) * -1))


################################################################

# method 1 vs. method 2

# code length: method 1 (135 B) < method 2 (287 B)
# memory used: same
# time taken: unavailable (test cases are different)