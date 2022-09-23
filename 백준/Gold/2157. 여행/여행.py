N, M, K = map(int,input().split())
meal = [[0]*(N+1) for _ in range(N+1)]
for i in range(K):
    a,b,c = map(int,input().split())
    meal[a][b] = max(meal[a][b],c)

board = [[0]*(M+1) for _ in range(N+1)]

# 1에서 출발 -> i도시에 한 번에 도착
for i in range(2, N+1):
    board[i][2] = meal[1][i]

for i in range(2,N+1): # N도시에 도착 해야함
    for j in range(3,M+1): # 최대 M개국 방문 ok (1 - 0 / 2 - 셋팅)
        for k in range(1,i):
            if meal[k][i] != 0 and board[k][j-1] != 0: # 기내식점수 있고, 이전점 밟은적 있을 때
                board[i][j] = max(board[k][j-1] + meal[k][i], board[i][j])

# print(board)
print(max(board[N]))