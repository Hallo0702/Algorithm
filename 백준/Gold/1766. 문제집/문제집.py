import heapq
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
pre = [0 for _ in range(N+1)]

for i in range(M):
    first, last = map(int, input().split())
    arr[first].append(last)
    pre[last] += 1

q = []

for i in range(1,N+1):
    if pre[i] == 0:
        heapq.heappush(q,i)

result = []

while q:
    now = heapq.heappop(q)

    result.append(now)
    for num in arr[now]:
        pre[num] -= 1
        if pre[num] == 0:
            heapq.heappush(q,num)

print(*result)