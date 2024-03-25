import sys
input = sys.stdin.readline


def find(x):
    if x != unions[x]:
        unions[x] = find(unions[x])
    return unions[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        unions[a] = b
    else:
        unions[b] = a


def solve():
    global unions
    n, m = map(int, input().split())
    unions = [i for i in range(n+1)]
    result = 0

    for i in range(m):
        x, y = map(int, input().split())
        union(x,y)

    for i in range(3,n+1):
        if unions[i] != unions[2]:
            break
    else:
        print("0 0")
        return

    arr = [list(map(int, input().split())) for _ in range(n)]

    q = []
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == j:
                continue

            q.append((arr[i][j],i+1,j+1))

    q.sort(key = lambda x:x[0])

    link = []
    for exp, x, y in q:
        a = find(x)
        b = find(y)

        if a != b:
            if a > b:
                unions[a] = b
            else:
                unions[b] = a
            result += exp
            link.append((x, y))

    print(result, len(link))
    for a, b in link:
        print(a, b)


solve()
