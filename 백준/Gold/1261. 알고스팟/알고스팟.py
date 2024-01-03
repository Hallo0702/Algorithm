from collections import deque
M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]

def bfs():
    global visit
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    q = deque()
    q.append((0, 0))
    visit[0][0] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            y2 = y + dy[i]
            x2 = x + dx[i]
            if y2 < 0 or y2 >= N or x2 < 0 or x2 >= M: continue
            if visit[y2][x2] == -1:
                if arr[y2][x2] == 0:
                    visit[y2][x2] = visit[y][x]
                    q.appendleft((y2,x2))
                elif arr[y2][x2] == 1:
                    visit[y2][x2] = visit[y][x] + 1
                    q.append((y2,x2))


bfs()
print(visit[N-1][M-1])

