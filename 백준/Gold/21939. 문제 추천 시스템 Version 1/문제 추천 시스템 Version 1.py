import sys
import heapq
input = sys.stdin.readline

max_h = []
min_h = []
check = {}

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_h,(-L,-P))
    heapq.heappush(min_h,(L,P))
    check[P] = L

M = int(input())
for _ in range(M):
    order = input().split()
    if order[0] == 'recommend':
        if order[1] == '1':
            while check[-max_h[0][1]] != -max_h[0][0]:
                heapq.heappop(max_h)
            print(-max_h[0][1])
        else:
            while check[min_h[0][1]] != min_h[0][0]:
                heapq.heappop(min_h)
            print(min_h[0][1])

    elif order[0] == 'solved':
        P = int(order[1])
        check[P] = 0

    elif order[0] == 'add':
        P = int(order[1])
        L = int(order[2])
        check[P] = L
        heapq.heappush(max_h,(-L,-P))
        heapq.heappush(min_h,(L,P))
