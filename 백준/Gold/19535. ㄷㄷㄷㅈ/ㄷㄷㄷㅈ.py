import sys
input = sys.stdin.readline

N = int(input())
degree = [0] * (N+1)
cnt_d = 0
cnt_g = 0
edge = []
for i in range(N-1):
    u, v = map(int, input().split())
    edge.append((u,v))
    degree[u] += 1
    degree[v] += 1

for i in range(1,N+1):
    if degree[i] >= 3:
        cnt_g += (degree[i] * (degree[i] -1) * (degree[i] - 2)) // 6

for ed in edge:
    if degree[ed[0]] >= 2 and degree[ed[1]] >= 2:
        cnt_d += (degree[ed[0]]-1) * (degree[ed[1]]-1)

if cnt_d > cnt_g * 3:
    print("D")
elif cnt_d < cnt_g * 3:
    print("G")
else:
    print("DUDUDUNGA")