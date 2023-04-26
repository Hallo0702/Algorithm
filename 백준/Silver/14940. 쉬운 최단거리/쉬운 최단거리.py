from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

answer = [[-1 for _ in range(m)] for _ in range(n)]


def bfs(idx_x,idx_y):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q = deque()
    q.append((idx_x,idx_y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if x2 >= 0 and x2 < n and y2 >= 0 and y2 < m and answer[x2][y2] == -1:
                q.append((x2,y2))
                answer[x2][y2] = answer[x][y] + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer[i][j] = 0
        elif arr[i][j] == 2:
            start_x = i
            start_y = j
            answer[i][j] = 0

bfs(start_x,start_y)

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()