import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [input().rstrip() for _ in range(N)]
dist = {}


def find_key(S):

    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0,S[0],S[1]))
    visited[S[0]][S[1]] = 1
    key_count = 0

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        cnt, x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx < N-1 and 0 < ny < N-1 and visited[nx][ny] == 0 and maze[nx][ny] != '1':
                if maze[nx][ny] == 'K':
                    if S not in dist:
                        dist[S] = []
                    dist[S].append((cnt+1,nx,ny))
                    key_count += 1
                q.append((cnt+1,nx,ny))
                visited[nx][ny] = 1

    return key_count



keys = []
for i in range(1,N-1):
    for j in range(1,N-1):
        if maze[i][j] == 'S':
            start = (i,j)

        if maze[i][j] == 'K':
            keys.append((i,j))

kc = find_key(start)
if kc != M:
    print('-1')
else:
    for key in keys:
        kc = find_key(key)

    visit = [[0 for _ in range(N)] for _ in range(N)]
    key_cnt = 0
    answer = 0
    hq = dist[start]
    heapq.heapify(hq)

    while hq:
        d, x, y = heapq.heappop(hq)
        if visit[x][y] == 0:
            visit[x][y] = 1
            key_cnt += 1
            answer += d

            if key_cnt == M:
                break

            for nd, nx, ny in dist[(x,y)]:
                if visit[nx][ny] == 0:
                    heapq.heappush(hq,(nd,nx,ny))

    print(answer)

