from collections import deque

Y, X = map(int, input().split())
MAP = [list(input()) for _ in range(Y)]
tmp = []
for y in range(Y):
    for x in range(X):
        if MAP[y][x] == 'o':
            tmp.append([y, x])

coins = deque()
coins.append((tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], 1))

def bfs():
    while coins:
        y1, x1, y2, x2, lev = coins.popleft()

        if lev > 10:
            return -1

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny1, nx1, ny2, nx2 = y1 + dy, x1 + dx, y2 + dy, x2 + dx

            #범위 안
            if 0 <= ny1 < Y and 0 <= nx1 < X and 0 <= ny2 < Y and 0 <= nx2 < X:
                if MAP[ny1][nx1] == '#':
                    ny1, nx1 = y1, x1

                if MAP[ny2][nx2] == '#':
                    ny2, nx2 = y2, x2

                coins.append((ny1, nx1, ny2, nx2, lev + 1))

            #하나만 떨어짐
            elif 0 <= ny1 < Y and 0 <= nx1 < X:
                return lev

            elif 0 <= ny2 < Y and 0 <= nx2 < X:
                return lev

            #둘 다 떨어짐
            else:
                continue

    return -1

print(bfs())