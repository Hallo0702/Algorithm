import sys
input=sys.stdin.readline


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

cnt = 0
diy = [-1, 1, 0, 0]
dix = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        for l in range(4):
            dy = i + diy[l]
            dx = j + dix[l]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[i][j] != arr[dy][dx]:
                    cnt+=1
                    break
tmp = 2**(N*M-cnt)
answer = tmp%(1000000007)
print(answer)