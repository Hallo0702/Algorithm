from collections import deque

a, b, c = map(int,input().split())

total = a + b + c


def bfs(total,a,b):
    q = deque()
    visit = [[0 for _ in range(total+1)] for _ in range(total+1)]
    q.append((a,b))
    visit[a][b] = 1

    while q:
        x, y = q.popleft()
        z = total - x - y

        if x == y and y == z:
            print(1)
            return

        for i, j in ((x,y),(x,z),(z,y)):

            if i == j:
                continue
            else:
                i -= j
                j += j

            k = total - i - j

            nx = max(i, j, k)
            ny = min(i, j, k)

            if visit[nx][ny] == 0:
                q.append((nx,ny))
                visit[nx][ny] = 1

    print(0)
    return


if total % 3 != 0:
    print(0)
else:
    bfs(total,max(a,b,c),min(a,b,c))