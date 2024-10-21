DP = [[0 for _ in range(31)] for _ in range(31)]

for j in range(31):
    DP[0][j] = 1

for j in range(31):
    for i in range(1,j+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

while 1:
    num = int(input())
    if num == 0:
        break

    print(DP[num][num])