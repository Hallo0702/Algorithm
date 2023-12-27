import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
sup = [0] + list(map(int, input().split()))
load = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for i in range(2,n+1):
    load[sup[i]].append(i)

for i in range(m):
    idx, w = map(int, input().split())
    answer[idx] += w


def dfs(num):
    for load_idx in load[num]:
        answer[load_idx] += answer[num]
        dfs(load_idx)


dfs(1)

print(*answer[1::])
