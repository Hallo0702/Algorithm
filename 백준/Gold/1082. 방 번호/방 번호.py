from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())

DP = [0] * (M+1)
q = deque()

for i in range(1,N):
    if P[i] <= M:
        q.append((i,P[i]))
        DP[P[i]] = i

while q:
    number, price = q.popleft()
    if DP[price] > number:
        continue

    for j in range(N):
        next_num = int(str(number)+str(j))
        if price + P[j] <= M and DP[price + P[j]] < next_num:
            DP[price+P[j]] = next_num
            q.append((next_num,price+P[j]))

print(max(DP))
