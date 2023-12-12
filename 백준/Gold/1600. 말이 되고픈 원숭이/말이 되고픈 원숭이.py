from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]

def bfs():
    hmx = [-2,-1,1,2,-2,-1,1,2]
    hmy = [1,2,2,1,-1,-2,-2,-1]

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]


    q = deque()
    q.append([0,0,0])

    visit = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    visit[0][0][0] = 1

    while q:
        nowy, nowx, cnt = q.popleft()
        if nowy == H-1 and nowx == W-1 :
            return visit[nowy][nowx][cnt]-1


        if cnt < K :
            for idx in range(8):
                ny = nowy + hmy[idx]
                nx = nowx + hmx[idx]

                if ny < 0 or ny >= H or nx < 0 or nx >= W : continue
                if visit[ny][nx][cnt+1] != 0 : continue
                if board[ny][nx] == 0 :
                    visit[ny][nx][cnt+1] = visit[nowy][nowx][cnt] + 1
                    q.append([ny,nx,cnt+1])

        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]
            if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
            if visit[ny][nx][cnt] != 0: continue
            if board[ny][nx] == 0:
                visit[ny][nx][cnt] = visit[nowy][nowx][cnt] + 1
                q.append([ny,nx,cnt])

    return -1

print(bfs())