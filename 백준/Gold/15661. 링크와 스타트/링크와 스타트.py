import sys
input = sys.stdin.readline


def stat_team():
    global answer
    team_stat = [0,0]
    for i in range(N):
        for j in range(i+1,N):
            if team[i] == team[j]:
                team_stat[team[i]] += stat[i][j]
    answer = min(answer,abs(team_stat[0]-team_stat[1]))
    return


def NoP(num):
    if num == N:
        stat_team()
        return

    team[num] = 0
    NoP(num+1)
    team[num] = 1
    NoP(num+1)


N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        stat[i][j] += stat[j][i]

team = [0 for _ in range(N)]
answer = sys.maxsize

NoP(0)
print(answer)