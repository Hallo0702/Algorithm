N,K = map(int, input().split())
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if i == 1:
            DP[i][j] = j
        else:
            DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % 1000000000

print(DP[N][K])