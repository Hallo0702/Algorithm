N, M = map(int, input().split())
arr = [[0 for _ in range(M+2)]] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0 for _ in range(M+2)]]
visit = [[0 for _ in range(M+2)] for _ in range(N+2)]

def dfs(y,x,level,total):
    global result, visit
    if level == 3:
        if result < total+arr[y][x]:
            result = total + arr[y][x]
        return

    visit[y][x] = 1
    for i in range(4):
        y2 = y + dy[i]
        x2 = x + dx[i]
        if 0 < y2 <= N and 0 < x2 <= M and visit[y2][x2] == 0:
            dfs(y2,x2,level+1,total+arr[y][x])
    visit[y][x] = 0


result = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]
for i in range(1,N+1):
    for j in range(1,M+1):
        dfs(i, j, 0, 0)
        a = arr[i-1][j]
        b = arr[i][j+1]
        c = arr[i+1][j]
        d = arr[i][j-1]
        e = arr[i][j]

        result = max(result,a+b+c+e,a+b+d+e,a+c+d+e,b+c+d+e)

print(result)
