import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewel = []

for i in range(N):
    heapq.heappush(jewel,list(map(int, input().split())))

bags = []
for i in range(K):
    bags.append(int(input()))
bags.sort()

prob_jewel = []

answer = 0

for bag in bags:
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(prob_jewel, -heapq.heappop(jewel)[1])
    
    if prob_jewel:
        answer -= heapq.heappop(prob_jewel)

print(answer)
