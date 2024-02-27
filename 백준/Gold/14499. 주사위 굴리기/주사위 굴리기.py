def change(dir): # 주사위 굴렸을 때의 위치 변화
    if dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif dir == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

dice = [0]*6 # 주사위 6칸
N, M, X, Y, K = map(int, input().split())
board = []
dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 1~4까지 차례로 동 서 북 남 이동

for _ in range(N):
    board.append(list(map(int, input().split())))

roll = list(map(int, input().split()))

for r in roll:
    dx, dy = X+dir[r][0], Y+dir[r][1] # X와 Y를 움직여 보고
    if 0 <= dx < N and 0 <= dy < M: # 범위 내이면
        change(r) # 주사위 칸 위치 바꿔주고
        if board[dx][dy] == 0: # 만약 움직인 곳의 숫자가 0이면
            board[dx][dy] = dice[5] # 주사위 아래 칸의 숫자를 복사
        else: # 아니면
            dice[5] = board[dx][dy] # 주사위 아래 칸의 숫자를 움직인 곳의 숫자로 변경하고
            board[dx][dy] = 0 # 움직인 곳을 0으로 변경
        print(dice[0]) # 주사위 윗칸 프린트
        X, Y = dx, dy # X, Y 를 움직인 곳으로 변경