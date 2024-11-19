import math
import heapq
import sys

input = sys.stdin.readline


def cal_distance(A,B):
    return math.sqrt(((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))

N, W = map(int, input().split())
M = float(input())

power_station = []
graph = [[] for _ in range(N)]
for n in range(N):
    x, y = map(int, input().split())
    power_station.append((x,y))

check = [[] for _ in range(N)]
for w in range(W):
    a, b = map(int, input().split())
    check[a-1].append(b-1)
    check[b-1].append(a-1)

distance = [sys.maxsize] * N
distance[0] = 0

for i in range(N):
    for j in range(i+1,N):
        if j in check[i]:
            graph[i].append((j,0))
            graph[j].append((i,0))
        else:
            dist = cal_distance(power_station[i],power_station[j])
            graph[i].append((j,dist))
            graph[j].append((i,dist))


def dijkstra(start):
    q = []
    q.append((0,start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next_node, next_dist in graph[node]:
            if distance[next_node] > dist + next_dist:
                distance[next_node] = dist + next_dist
                heapq.heappush(q,(dist+next_dist,next_node))

dijkstra(0)
print(int(1000*distance[N-1]))