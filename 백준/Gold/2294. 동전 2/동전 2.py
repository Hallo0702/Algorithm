from collections import deque


def sol():
    n, k = map(int,input().split())
    coins = set()
    q = deque()
    visit = [False] * (k+1)
    for i in range(n):
        coin = int(input())
        if coin < k:
            coins.add(coin)
            q.append((coin,1))
            visit[coin] = True
        elif coin == k:
            print(1)
            return
    coins = sorted(coins)
    if coins[0] > k:
        print(-1)
        return

    while q:
        c, t = q.popleft()
        for coin in coins:
            if c + coin > k:
                break
            elif c + coin == k:
                print(t+1)
                return
            if not visit[c+coin]:
                q.append((c+coin,t+1))
                visit[c+coin] = True

    print(-1)
    return

sol()