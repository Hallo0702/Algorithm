import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    visit = [[0 for _ in range(M)] for _ in range(N)]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    q = deque()
    q.append((0,0))
    visit[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            y2 = y + dy[i]
            x2 = x + dx[i]
            if 0 <= y2 < N and 0 <= x2 < M and visit[y2][x2] == 0:
                if arr[y2][x2] == 0:
                    q.append((y2,x2))
                    visit[y2][x2] = 1
                else:
                    arr[y2][x2] += 1


time = 0
while True:
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                flag = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
    
    if flag == 1:
        time += 1
    else:
        break

print(time)

