import sys
sys.setrecursionlimit(10**7)

T = int(input())


def dfs(idx):
    global answer

    if visit[idx] == 0:
        visit[idx] = 1
        team.append(idx)
        dfs(select[idx])
        return
    else:
        if idx in team:
            answer += len(team[team.index(idx):])
        return


for _ in range(T):
    n = int(input())
    select = [0]+list(map(int, input().split()))
    answer = 0
    visit = [0] * (n+1)
    for i in range(1,n+1):
        if visit[i] == 0:
            team = []
            dfs(i)

    print(n-answer)