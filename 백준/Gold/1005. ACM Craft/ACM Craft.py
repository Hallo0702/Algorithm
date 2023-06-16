import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def ACM():
    N, K = map(int, input().split())

    building_time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    deg = [0 for _ in range(N+1)]
    done_time = [0 for _ in range(N+1)]

    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        deg[b] += 1

    W = int(input())

    if deg[W] == 0:
        print(building_time[W])
        return

    q = deque()

    for i in range(1,N+1):
        if deg[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        done_time[now] = done_time[now] + building_time[now]

        for next in graph[now]:
            done_time[next] = max(done_time[now],done_time[next])
            deg[next] -= 1
            if deg[next] == 0:
                if next == W:
                    print(done_time[next]+building_time[next])
                    return
                else:
                    q.append(next)


for _ in range(T):
    ACM()