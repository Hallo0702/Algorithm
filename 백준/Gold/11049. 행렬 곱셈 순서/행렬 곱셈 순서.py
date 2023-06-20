import sys
input = sys.stdin.readline

N = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(N)]
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1,N):
    for j in range(0,N-i):

        DP[j][j+i] = sys.maxsize
        for k in range(j,j+i):
            DP[j][j+i] = min(DP[j][j+i], DP[j][k] + DP[k+1][j+i] + (matrix[j][0] * matrix[k][1] * matrix[j+i][1]))


print(DP[0][N-1])