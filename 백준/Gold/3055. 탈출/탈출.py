import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]
q = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i,j,-1))

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            q.append((i,j,0))
        elif arr[i][j] == 'D':
            Dx, Dy = i, j


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y, time = q.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if time == -1 and (arr[nx][ny] == '.' or arr[nx][ny] == 'S'):
                    arr[nx][ny] = '*'
                    q.append((nx,ny,-1))

                elif time >= 0 and (arr[nx][ny] == '.'):
                    arr[nx][ny] = 'S'
                    q.append((nx,ny,time+1))

                elif time >= 0 and (arr[nx][ny] == 'D'):
                    return time + 1

    return "KAKTUS"

print(bfs())