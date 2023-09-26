import sys
import heapq
input = sys.stdin.readline
n = int(input())

q = []
check = [False] * (10001)

for _ in range(n):
    p, d = map(int, input().split())

    heapq.heappush(q,(-p,d))

answer = 0
flag = 0
while q:
    p, d = heapq.heappop(q)

    for day in range(d,0,-1):
        if check[day] == False:
            check[day] = True
            flag += 1
            answer += -p
            break

print(answer)