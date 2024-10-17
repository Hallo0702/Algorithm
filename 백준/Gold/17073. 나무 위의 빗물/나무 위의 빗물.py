import sys
input = sys.stdin.readline

N, W = map(int,input().split())

graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]

for i in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

cnt = 0
for i in range(2,N+1):
    if len(graph[i]) == 1:
        cnt += 1

answer = W / cnt
print(answer)