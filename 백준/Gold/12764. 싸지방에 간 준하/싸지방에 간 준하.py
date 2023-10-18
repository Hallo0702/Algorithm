import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
    start, end = map(int, input().rstrip().split())
    heapq.heappush(q,(start,end))

computer = [0] * N
cnt = [0] * N

while q:
    start, end = heapq.heappop(q)

    for i in range(N):
        if computer[i] <= start:
            cnt[i] += 1
            computer[i] = end
            break

if computer[-1] == 0:
    X = computer.index(0)
else:
    X = N
print(X)
print(' '.join(map(str,cnt[:X])))