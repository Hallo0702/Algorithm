import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    k, n = map(int, input().split())
    weights = []
    for i in range(4):
        weights.append(list(map(int, input().split())))

    first = set()
    second = set()

    for i in range(n):
        for j in range(n):
            first.add(weights[0][i] + weights[1][j])
            second.add(weights[2][i] + weights[3][j])

    first = sorted(list(first))
    second = sorted(list(second))

    start = 0
    end = len(second) - 1

    d = sys.maxsize
    res = sys.maxsize

    while start < len(first) and end >= 0:

        if abs(first[start] + second[end] - k) < d:
            d = abs(first[start] + second[end] - k)
            res = first[start] + second[end]

        elif abs(first[start] + second[end] - k) == d:
            res = min(res,first[start] + second[end])

        if first[start] + second[end] > k:
            end -= 1
        elif first[start] + second[end] < k:
            start += 1
        else:
            break

    print(res)