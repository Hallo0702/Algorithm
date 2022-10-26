import heapq

N, M, K = map(int, input().split())

cable = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

power = list(map(int, input().split()))

for i in range(M):
    u, v, w = map(int, input().split())
    cable[u].append((w,v))
    cable[v].append((w,u))

q = []
for p in power:
    visit[p] = 1
    for c in cable[p]:
        heapq.heappush(q,c)

answer = 0
while q:
    w, next = heapq.heappop(q)
    if visit[next] == 1:
        continue

    answer += w
    visit[next] = 1
    for c in cable[next]:
        heapq.heappush(q,c)

print(answer)