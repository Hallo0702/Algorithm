import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
v = [int(input()) for _ in range(N)]
DP = [[0] * N for _ in range(N)]


def harvest(left,right,cnt):
    if left > right:
        return 0
    if DP[left][right] != 0:
        return DP[left][right]
    DP[left][right] = max(v[left]*cnt+harvest(left+1,right,cnt+1),
                          v[right]*cnt+harvest(left,right-1,cnt+1))
    return DP[left][right]

print(harvest(0,N-1,1))