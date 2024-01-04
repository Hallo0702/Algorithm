import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
room = [list(input().rstrip()) for _ in range(N)]
inf = sys.maxsize
visit = [[inf] * M for _ in range(N)]
visit[x1][y1] = 0
q = [(0,x1,y1)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    time, now_x, now_y = heapq.heappop(q)

    if time > visit[now_x][now_y]:
        continue

    if now_x == x2 and now_y == y2:
        print(visit[now_x][now_y])
        break

    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if room[next_x][next_y] == '0' and visit[next_x][next_y] > time:
                visit[next_x][next_y] = time
                heapq.heappush(q,(time,next_x,next_y))

            elif (room[next_x][next_y] == '1' or  room[next_x][next_y] == '#')and visit[next_x][next_y] > time + 1:
                visit[next_x][next_y] = time + 1
                heapq.heappush(q, (time+1, next_x, next_y))

