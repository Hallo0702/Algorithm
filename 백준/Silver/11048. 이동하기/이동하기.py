import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = max(DP[i-1][j],DP[i][j-1]) + maze[i-1][j-1]

print(DP[N][M])