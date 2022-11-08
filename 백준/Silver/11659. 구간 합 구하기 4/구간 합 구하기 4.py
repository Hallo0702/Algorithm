import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
total = [0 for _ in range(N+1)]
for i in range(0,N):
    total[i+1] = total[i] + arr[i]

for i in range(M):
    a, b = map(int, input().split())
    print(total[b]-total[a-1])
