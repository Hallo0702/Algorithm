n, k = map(int,input().split())
coins = set()
for i in range(n):
    coins.add(int(input()))

coins = sorted(list(coins))

DP = [-1] * (k+1)
DP[0] = 0

for i in range(1,k+1):

    for coin in coins:
        if i - coin < 0:
            break

        if DP[i - coin] >= 0:
            if DP[i] == -1:
                DP[i] = DP[i-coin] + 1
            else:
                DP[i] = min(DP[i],DP[i-coin]+1)

print(DP[k])