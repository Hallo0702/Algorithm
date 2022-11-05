def gcd(a, b):
    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a


T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    big = gcd(a, b)
    lcs = big * (a // big) * (b // big)
    print(lcs)
