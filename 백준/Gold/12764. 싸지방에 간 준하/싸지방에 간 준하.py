import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = sorted([tuple(map(int, input().split())) for _ in range(N)], key= lambda x: x[0])

computer = []
possible = []
cnt = [0] * N

for start, end in q:

    while computer and computer[0][0] <= start:
        last_end, idx = heapq.heappop(computer)
        heapq.heappush(possible, idx)

    if not possible:
        idx = len(computer)
    else:
        idx = heapq.heappop(possible)

    heapq.heappush(computer,(end,idx))
    cnt[idx] += 1

if cnt[-1] == 0:
    X = cnt.index(0)
else:
    X = N
print(X)
print(' '.join(map(str,cnt[:X])))