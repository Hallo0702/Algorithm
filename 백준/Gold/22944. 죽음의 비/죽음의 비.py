import sys
from collections import deque
input = sys.stdin.readline


N, H, D = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

start_x, start_y = -1, -1
for x in range(N):
    for y in range(N):
        if arr[x][y] == 'S':
            start_x, start_y = x, y


def solve():
    health = [[0 for _ in range(N)] for _ in range(N)]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    health[start_x][start_y] = H
    q = deque()
    q.append((start_x,start_y,H,0,0))

    while q:
        now_x, now_y, now_h, now_d, ans = q.popleft()

        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]

            if not check(next_x,next_y):
                continue

            if arr[next_x][next_y] == 'E':
                return ans+1

            next_h = now_h
            next_d = now_d

            if arr[next_x][next_y] == 'U':
                next_d = D

            if next_d == 0:
                next_h -= 1
            else:
                next_d -= 1

            if next_h > 0:
                if health[next_x][next_y] < next_h + next_d:
                    health[next_x][next_y] = next_h + next_d
                    q.append((next_x,next_y,next_h,next_d,ans+1))

    return -1


def check(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


print(solve())