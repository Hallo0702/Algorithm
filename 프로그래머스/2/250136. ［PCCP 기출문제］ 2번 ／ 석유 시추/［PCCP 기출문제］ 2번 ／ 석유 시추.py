from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    check = [[0 for _ in range(m)] for _ in range(n)]
    amount = [0 for _ in range(m)]

    def bfs(x, y):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        q = deque()
        q.append((x,y))
        check[x][y] = 1
        y1, y2 = y, y
        cnt = 0

        while q:
            now_x, now_y = q.popleft()
            y1 = min(y1, now_y)
            y2 = max(y2, now_y)
            cnt += 1
            for i in range(4):
                next_x, next_y = now_x + dx[i], now_y + dy[i]
                if 0 <= next_x < n and 0 <= next_y < m and land[next_x][next_y] == 1 and check[next_x][next_y] == 0:
                    check[next_x][next_y] = 1
                    q.append((next_x, next_y))

        for i in range(y1, y2+1):
            amount[i] += cnt

        return

    for i in range(n):
        for j in range(m):
            if check[i][j] == 0 and land[i][j] == 1:
                bfs(i, j)

    answer = max(amount)
    return answer
