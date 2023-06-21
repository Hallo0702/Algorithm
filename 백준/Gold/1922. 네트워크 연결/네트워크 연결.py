import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
graph = []

def find(node):
    if node == parent[node]:
        return node

    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(graph,(c,a,b))

answer = 0
for i in range(M):
    w, a, b = heapq.heappop(graph)

    if find(a) != find(b):
        union(a, b)
        answer += w

print(answer)
