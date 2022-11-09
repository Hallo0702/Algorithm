import heapq
import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    X = int(input())
    if X == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr,-X)