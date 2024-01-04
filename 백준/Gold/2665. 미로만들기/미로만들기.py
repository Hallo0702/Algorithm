import heapq
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def dks():
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        cnt, cy, cx = heapq.heappop(pq)

        if cy == N-1 and cx == N-1:
           return cnt

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    if graph[ny][nx] == 1:
                        heapq.heappush(pq, (cnt, ny, nx))
                    elif graph[ny][nx] == 0:
                        heapq.heappush(pq, (cnt + 1, ny, nx))

print(dks())