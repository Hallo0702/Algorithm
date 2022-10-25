from collections import deque

def farthestNode(node):
    visit = [-1 for _ in range(N+1)]
    visit[node] = 0
    q = deque()
    q.append(node)

    while q:
        nowNode = q.popleft()

        for nextNode, w in graph[nowNode]:
            if visit[nextNode] == -1:
                visit[nextNode] = visit[nowNode] + w
                q.append(nextNode)

    return visit.index(max(visit))

def secondLongLength(node,exceptNode):
    visit = [-1 for _ in range(N + 1)]
    visit[node] = 0
    q = deque()
    q.append(node)

    while q:
        nowNode = q.popleft()

        for nextNode, w in graph[nowNode]:
            if visit[nextNode] == -1:
                visit[nextNode] = visit[nowNode] + w
                q.append(nextNode)

    visit[exceptNode] = 0

    return max(visit)

global graph, N

N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2,weight))
    graph[node2].append((node1,weight))

first_l = farthestNode(1)
first_r = farthestNode(first_l)

second_l = secondLongLength(first_l,first_r)
second_r = secondLongLength(first_r,first_l)
answer = max(second_r,second_l)
print(answer)