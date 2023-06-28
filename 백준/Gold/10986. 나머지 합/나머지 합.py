import sys
from collections import defaultdict
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = defaultdict(int)
pre_sum = 0
cnt[0] = 1
answer = 0

for i in range(N):
    pre_sum = (pre_sum + arr[i]) % M
    cnt[pre_sum] += 1


for c in cnt.values():
    answer += c * (c-1) // 2

print(answer)
