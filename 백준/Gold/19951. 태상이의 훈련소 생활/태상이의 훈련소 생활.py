import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ground = list(map(int, input().split()))
dig = [0] * (N+1)
for m in range(M):
    a, b, k = map(int, input().split())
    dig[a-1] += k
    dig[b] -= k

for n in range(1,N):
    dig[n] += dig[n-1]

for i in range(N):
    ground[i] += dig[i]

print(*ground)



