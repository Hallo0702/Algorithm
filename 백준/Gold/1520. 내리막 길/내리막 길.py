import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(y,x):
    global cnt
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    if y == M-1 and x == N-1:
        return 1

    if cnt[y][x] != -1:
        return cnt[y][x]

    tmp = 0
    for i in range(4):
        y2 = y + dy[i]
        x2 = x + dx[i]
        if 0 <= y2 < M and 0 <= x2 < N:
            if arr[y][x] > arr[y2][x2]:
                tmp += dfs(y2,x2)

    cnt[y][x] = tmp
    return cnt[y][x]

print(dfs(0,0))