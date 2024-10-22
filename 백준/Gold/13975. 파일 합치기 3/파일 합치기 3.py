import heapq
import sys
input = sys.stdin.readline


T = int(input())

for t in range(T):
    K = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)

    answer = 0

    for _ in range(K-1):
        num1 = heapq.heappop(q)
        num2 = heapq.heappop(q)

        answer += num1 + num2

        heapq.heappush(q,num1+num2)

    print(answer)