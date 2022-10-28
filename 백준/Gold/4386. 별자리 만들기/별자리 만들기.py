import sys
import math
import heapq
input = sys.stdin.readline


def find_boss(x):
    global boss
    if boss[x] != x:
        boss[x] = find_boss(boss[x])
    return boss[x]


def union(x, y):
    a = find_boss(x)
    b = find_boss(y)

    if a < b:
        boss[a] = boss[b]
    else:
        boss[b] = boss[a]


N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]
d = []

for i in range(N-1):
    for j in range(i+1,N):
        distance = math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2)
        heapq.heappush(d,(distance,i,j))

global boss
answer = 0
boss = [i for i in range(N)]
cnt = 1

while d:
    w, x, y = heapq.heappop(d)
    if find_boss(x) != find_boss(y):
        union(x,y)
        answer += w
        cnt += 1

    if cnt == N:
        break

print(round(answer,2))
