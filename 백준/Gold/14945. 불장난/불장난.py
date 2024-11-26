N = int(input())

if N == 1:
    print(1)
else:
    DP = [[0] * (N + 1) for _ in range(N + 1)]  # [층수][탈출 위치 사이 거리]
    DP[1][0] = 1
    DP[2][1] = 1
    for i in range(3,N+1):
        for j in range(1,N):
            DP[i][j] = ((DP[i - 1][j] * 2) + DP[i - 1][j + 1] + DP[i - 1][j - 1]) % 10007
    print((sum(DP[N])*2)%10007)

