import sys
input = sys.stdin.readline

N = int(input())
    
nums = sorted(list(map(int, input().split())))

ans = 0

for i in range(len(nums)):
    ans += sum(nums[:i+1])
    
print(ans)