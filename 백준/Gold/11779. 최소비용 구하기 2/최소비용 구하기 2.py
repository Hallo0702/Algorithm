import heapq
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
roots = [[] for _ in range(N+1)]
inf = int(1e9)
result = [inf for _ in range(N+1)]

for i in range(M):
    s, e, w = map(int, input().split())
    arr[s].append((e,w))

start, end = map(int, input().split())

q = []
heapq.heappush(q,(0,start))
result[start] = 0
roots[start].append(start)

while q:
    wei, now = heapq.heappop(q)
    if wei > result[now]: continue

    for target, we in arr[now]:
        cnt = we + wei
        if cnt < result[target]:
            result[target] = cnt
            roots[target] = roots[now] + [target]
            heapq.heappush(q,(cnt, target))

print(result[end])
print(len(roots[end]))
print(*roots[end])