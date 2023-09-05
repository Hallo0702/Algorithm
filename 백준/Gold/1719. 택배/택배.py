import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[i for i in range(1,n+1)] for j in range(n)]
for i in range(n):
    arr[i][i] = '-'


graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))


def dijkstra(node):
    inf = sys.maxsize
    result = [inf for i in range(n+1)]

    q = []
    heappush(q,(0,node))
    result[node] = 0

    while q:
        time, area = heappop(q)

        if time > result[area]:
            continue

        for next_area, time_taken in graph[area]:
            if result[next_area] > time + time_taken:
                result[next_area] = time + time_taken
                heappush(q,(time+time_taken,next_area))
                if arr[node-1][area-1] != '-':
                    arr[node-1][next_area-1] = arr[node-1][area-1]


for i in range(1,n+1):
    dijkstra(i)

for i in range(n):
    print(*arr[i])