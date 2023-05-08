import heapq
import sys

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

def dijkstra(arr, start):
    inf = sys.maxsize
    distance = [inf for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))

    while q:
        now_d, now_idx = heapq.heappop(q)

        if distance[now_idx] < now_d:
            continue

        for next_d, next_idx in arr[now_idx]:
            d = next_d + now_d
            if d < distance[next_idx]:
                distance[next_idx] = d
                heapq.heappush(q,(d,next_idx))

    return distance


result = dijkstra(graph,1)
print(result[N])