import heapq
import sys
inf = sys.maxsize
input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())
root = [[] for _ in range(N+1)]
costs = set()

for _ in range(M):
    a, b, c = map(int, input().split())
    root[a].append((b,c))
    root[b].append((a,c))
    costs.add(c)
costs = list(costs)
costs.sort()


def dijkstra(max_cost):
    q = []
    distance = [inf for _ in range(N + 1)]
    distance[A] = 0
    heapq.heappush(q,(0,A))

    while q:
        now_cost, now_root = heapq.heappop(q)

        if distance[now_root] < now_cost:
            continue

        for next_root, next_cost in root[now_root]:
            if distance[next_root] > next_cost + now_cost and next_cost <= max_cost and next_cost + now_cost <= C:
                distance[next_root] = next_cost + now_cost
                heapq.heappush(q,(next_cost+now_cost,next_root))

    return distance[B]


left, right = 0, len(costs)-1
answer = inf
while left <= right:
    mid = (left + right) // 2
    total = dijkstra(costs[mid])
    if total == inf:
        left = mid + 1
    else:
        right = mid - 1
        answer = costs[mid]

if answer == inf:
    print(-1)
else:
    print(answer)