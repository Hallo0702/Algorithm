import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))


def dijk(node):
    inf = sys.maxsize
    length = [inf] * (n+1)
    length[node] = 0
    q = deque()
    q.append((0,node))

    while q:
        d, now = q.popleft()
        if length[now] < d:
            continue

        for next, next_l in graph[now]:
            if length[next] > length[now] + next_l:
                length[next] = length[now] + next_l
                heapq.heappush(q, (length[now] + next_l, next))


    result = 0
    for i in range(1,n+1):
        if length[i] <= m:
            result += items[i]


    return result


answer = 0
for i in range(1,n+1):
    answer = max(answer,dijk(i))

print(answer)