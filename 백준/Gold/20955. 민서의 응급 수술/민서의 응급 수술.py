import sys
input = sys.stdin.readline


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a <= b:
        root[b] = a
    else:
        root[a] = b


N, M = map(int, input().split())

root = [i for i in range(N+1)]
root_cnt = set()

cnt = 0
for i in range(M):
    u, v = map(int, input().split())

    if find(u) == find(v):
        cnt += 1
    else:
        union(u,v)


for i in range(1,N+1):
    root_cnt.add(find(i))

print(len(root_cnt)-1 + cnt)