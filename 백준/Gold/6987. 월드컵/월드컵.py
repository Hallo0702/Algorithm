from itertools import combinations

def matching(round):
    if round == 15:
        return 1

    team1, team2 = match[round]
    for a, b in ((0,2),(1,1),(2,0)):
        if wdl[a][team1] > 0 and wdl[b][team2] > 0:
            wdl[a][team1] -= 1
            wdl[b][team2] -= 1
            temp = matching(round+1)
            if temp == 1:
                return 1
            wdl[a][team1] += 1
            wdl[b][team2] += 1

    return 0



answer = []
match = list(combinations(range(6),2))

for i in range(4):
    arr = list(map(int, input().split()))
    if 6 in arr:
        answer.append(0)
        continue

    wdl = [arr[::3],arr[1::3],arr[2::3]]

    if sum(wdl[0]) + sum(wdl[1]) + sum(wdl[2]) != 30 or sum(wdl[0]) != sum(wdl[2]):
        answer.append(0)
        continue

    answer.append(matching(0))
print(*answer)

