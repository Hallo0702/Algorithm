import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sup = [0] + list(map(int, input().split()))
answer = [0] * (n+1)

for i in range(m):
    idx, w = map(int, input().split())
    answer[idx] += w

for i in range(2,n+1):
    answer[i] += answer[sup[i]]

print(*answer[1::])