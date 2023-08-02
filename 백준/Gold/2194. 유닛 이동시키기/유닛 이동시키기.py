from collections import deque

N, M, A, B, K = map(int, input().split())

arr = [[0 for _ in range(M+1)] for _ in range(N+1)]
visit = [[0 for _ in range(M+1)] for _ in range(N+1)]

for k in range(K):
    a, b = map(int, input().split())
    arr[a][b] = -1

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())


def is_block(x, y):
    for i in range(x,x+A):
        for j in range(y,y+B):
            if arr[i][j] == -1:
                return False

    return True


def bfs(x, y):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    q = deque()
    visit[x][y] = 1
    q.append((x,y,0))

    while q:
        nowX, nowY, res = q.popleft()

        if nowX == end_x and nowY == end_y:
            return res

        for i in range(4):
            nextX, nextY = nowX + dx[i], nowY + dy[i]
            if 1 <= nextX and nextX + A - 1 <= N and 1 <= nextY and nextY + B - 1 <= M and visit[nextX][nextY] == 0 and is_block(nextX,nextY):
                visit[nextX][nextY] = 1
                q.append((nextX,nextY,res+1))

    return -1


print(bfs(start_x,start_y))