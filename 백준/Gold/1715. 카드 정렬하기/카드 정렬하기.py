import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []

for i in range(N):
    heapq.heappush(q,int(input()))

cnt = 0

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    cnt += a+b

    heapq.heappush(q, a+b)

print(cnt)