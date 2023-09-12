import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))


def dfs(node, weight):
    for next_node, wei in graph[node]:
        if visit[next_node] == -1:
            visit[next_node] = weight + wei
            dfs(next_node,visit[next_node])


visit = [-1 for _ in range(n+1)]
visit[1] = 0
dfs(1,0)

start_node = visit.index(max(visit))
visit = [-1 for _ in range(n+1)]
visit[start_node] = 0
dfs(start_node,0)

print(max(visit))