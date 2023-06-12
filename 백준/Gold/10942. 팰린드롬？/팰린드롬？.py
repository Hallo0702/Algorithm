import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
palin = [[0 for _ in range(N)] for _ in range(N)]

for l in range(N):
    for s in range(N-l):
        e = s + l
        if numbers[s] == numbers[e]:
            if s + 2 > e:
                palin[s][e] = 1
            else:
                if palin[s+1][e-1] == 1:
                    palin[s][e] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(palin[S-1][E-1])

