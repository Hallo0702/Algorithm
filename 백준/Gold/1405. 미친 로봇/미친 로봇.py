N, e, w, s, n = map(int, input().split())

arr = [[0 for _ in range(2*N + 1)] for _ in range(2*N + 1)]
p = [e,w,s,n]

answer = 0

def dfs(x,y,percent,level):
    global answer

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    if percent == 0:
        return

    if level == N:
        answer += percent
        return

    arr[x][y] = 1

    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if 0 <= x2 < 2*N + 1 and 0 <= y2 < 2*N + 1:
            if arr[x2][y2] == 1:
                continue

            else:
                dfs(x2,y2,percent*(p[i]/100),level+1)

    arr[x][y] = 0


dfs(N,N,1,0)

print(answer)