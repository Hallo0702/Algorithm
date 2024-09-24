# 2번 최대 범위 먼저 구하고 풀기
from collections import deque
T = int(input())
nm = deque()
max_n, max_m = 0, 0
for t in range(T):
    n, m = map(int, input().split())
    if n > max_n:
        max_n = n
    if m > max_m:
        max_m = m
    nm.append((n,m))

DP = [[1]*(max_m+1)] + [[0]*(max_m+1) for _ in range(max_n+1)]

for i in range(1,max_n+1):
    for j in range(i,max_m+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j//2]

for N, M in nm:
    print(DP[N][M])
'''
# 1번 전체 구해놓고 하나씩 하기
T = int(input())
DP = [[1]*2001] + [[0]*2001 for _ in range(10)]

for i in range(1,11):
    for j in range(i,2001):
        DP[i][j] = DP[i][j-1] + DP[i-1][j//2]

for t in range(T):
    n, m = map(int, input().split())
    print(DP[n][m])
'''