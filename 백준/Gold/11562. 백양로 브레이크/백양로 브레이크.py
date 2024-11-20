import sys
input = sys.stdin.readline

N, M = map(int, input().split())

road = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1): # 같은 길은 우선 0 으로
    road[i][i] = 0

for m in range(M): # 한 방향 -> 0 / 1 양방향 0/0
    u, v, b = map(int, input().split())
    road[u][v] = 0
    if b == 0:
        road[v][u] = 1
    else:
        road[v][u] = 0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            road[i][j] = min(road[i][j],road[i][k]+road[k][j])

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    print(road[a][b])
