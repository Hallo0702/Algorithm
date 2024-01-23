import math
import sys
input = sys.stdin.readline

def find_d(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x**2 + y**2)


def dfs(now,total, visit):
    global answer
    if total >= answer:
        return
    if sum(visit) == n-1:
        result = total + distance[now][0]
        answer = min(result,answer)
        return
    for i in range(1,n):
        if visit[i] == 1:
            continue
        visit[i] = 1
        dfs(i,total+distance[now][i],visit)
        visit[i] = 0


n = int(input())
nations = [tuple(map(int,input().split())) for _ in range(n)]
distance = [[0 for _ in range(n)] for _ in range(n)]
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if i != j:
            distance[i][j] = find_d(nations[i],nations[j])

dfs(0,0,[0]*n)
print(answer)