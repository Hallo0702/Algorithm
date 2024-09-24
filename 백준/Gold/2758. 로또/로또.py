import sys
input = sys.stdin.readline

T = int(input())
DP = [[1]*2001] + [[0]*2001 for _ in range(10)]

for i in range(1,11):
    for j in range(i,2001):
        DP[i][j] = DP[i][j-1] + DP[i-1][j//2]

for t in range(T):
    n, m = map(int, input().split())
    print(DP[n][m])