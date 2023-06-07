import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = {}
    total = 0
    for i in range(N):
        coin, cnt = map(int, input().split())
        total += coin * cnt
        coins[coin] = cnt


    if total % 2 == 1:
        print(0)
        continue

    total //= 2

    dp = [1] + [0] * total

    for coin, cnt in coins.items():
        for now in range(total,coin-1,-1):
            if dp[now-coin] == 1:
                for c in range(cnt):
                    if now + coin * c <= total:
                        dp[now+coin*c] = 1

        if dp[total] == 1:
            break

    print(dp[total])