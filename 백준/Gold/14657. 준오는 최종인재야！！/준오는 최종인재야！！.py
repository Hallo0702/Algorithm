## 문제를 풀고 난 결과 -> 몇개의 문제를 풀었는가? 그만큼의 문제를 푸는데 몇 시간이 걸렸는가?
## 트리에서 가장 먼 거리를 찾는 과정 //
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node,cnt):
    global nodeCnt, endNode, minTime

    if nodeCnt < cnt: # 현재 진행 개수보다 높으면 갱신
        nodeCnt = cnt
        endNode = node
        minTime = visit[node]
    elif nodeCnt == cnt and visit[node] < minTime:
        endNode = node
        minTime = visit[node]

    for nextNode, time in graph[node]:
        if visit[nextNode] == -1:
            visit[nextNode] = visit[node] + time
            dfs(nextNode,cnt+1)


N, T = map(int, input().split())
## 연결 루트 기록
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

## 임의의 한 점에서 가장 먼 점을 찾으면 그게 트리에서 가장 긴 루트의 한쪽 끝이다. 임의로 1부터 시작한다고 치자.
nodeCnt, endNode, minTime = 1, 1, sys.maxsize
visit = [-1] * (N+1)
visit[1] = 0
dfs(1,1)


## endNode에 한쪽 끝점 찾음
## 이제 반대쪽 끝점을 찾아 시간을 구해주면 된다.
nodeCnt, minTime = 1, sys.maxsize
visit = [-1] * (N + 1)
visit[endNode] = 0
dfs(endNode,1)

print(math.ceil(minTime/T))