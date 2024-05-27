import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
pre = [ 0 for _ in range(N+1)]
post = [[] for _ in range(N+1)]
answer = []

for i in range(M):
    A, B = map(int, input().split())
    pre[B] += 1
    post[A].append(B)

q = []
for i in range(1,N+1):
    if pre[i] == 0:
        q.append(i)

while q:
    problem = heapq.heappop(q)
    answer.append(problem)
    for num in post[problem]:
        pre[num] -= 1
        if pre[num] == 0:
            heapq.heappush(q,num)

print(*answer)
