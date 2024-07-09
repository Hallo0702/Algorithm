import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sheet = [['0' for _ in range(20)] for _ in range(N)]
passlist = dict()
answer = 0


def first(i,x):
    sheet[i-1][x-1] = '1'


def second(i, x):
    sheet[i-1][x-1] = '0'


def third(i):
    for n in range(19,0,-1):
        sheet[i-1][n] = sheet[i-1][n-1]
    sheet[i-1][0] = '0'


def forth(i):
    for n in range(0,19):
        sheet[i-1][n] = sheet[i-1][n+1]
    sheet[i-1][19] = '0'


for m in range(M):
    order = list(map(int, input().split()))
    if order[0] == 1:
        first(order[1],order[2])
    elif order[0] == 2:
        second(order[1],order[2])
    elif order[0] == 3:
        third(order[1])
    else:
        forth(order[1])

for train in sheet:
    train_code = ''.join(train)
    if train_code not in passlist:
        answer += 1
        passlist[train_code] = 1

print(answer)