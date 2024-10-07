import sys
import heapq
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M): # 도로 입력 받기
    A, B, C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

q = [] # 다익스트라 사용해 각 집까지의 최소 거리 구함

inf = sys.maxsize
dt = [inf] * N
dt[Y] = 0
q.append((0,Y))
while q:
    now_d, now_node = heapq.heappop(q)

    if now_d > dt[now_node]:
        continue

    for next_node, c in graph[now_node]:
        if dt[next_node] > now_d + c:
            dt[next_node] = now_d + c
            heapq.heappush(q, (now_d+c,next_node))

dt.sort() # 거리순서대로 진행하기 위해 정렬
if dt[-1] * 2 > X: # 만약 가장 먼 집의 왕복거리가 X보다 멀면 방문할 수 없으므로 -1 출력
    print(-1)
else:
    answer = 1 # 1일차 부터 시작
    temp = X
    for i in range(N):
        if temp >= 2 * dt[i]: # 남은 거리가 왕복 가능한 거리면 왕복
            temp -= 2 * dt[i]
        else:
            answer += 1 # 불가능한 거리면 다음날로 바꾸고 왕복
            temp = X - (2 * dt[i])

    print(answer)

