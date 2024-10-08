import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())

DP = [0] * (M+1)

for i in range(N-1,-1,-1):
    for j in range(P[i],M+1):
        DP[j] = max(DP[j], DP[j - P[i]]*10+i)

print(max(DP))
