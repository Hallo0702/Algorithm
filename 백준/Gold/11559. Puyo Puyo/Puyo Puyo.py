from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def gravity(): # 밑으로 떨어트리기
    for x in range(6):
        q = deque()
        for y in range(11, -1, -1):
            if board[y][x] != '.':
                q.append(board[y][x]) # 아래에서부터 차례로 색상 담기
        for y in range(11, -1, -1):
            if q:
                board[y][x] = q.popleft() # 차례로 색상 꺼내기
            else:
                board[y][x] = "."

def BFS(y,x): # 연결되어 있는 같은 색상 => 터트리기
    check = [[0]*6 for _ in range(12)]
    q = deque()
    boom = deque()
    q.append((y, x))
    boom.append((y, x))
    target = board[y][x]
    check[y][x] = 1
    while q:
        ny, nx = q.popleft()
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < 12 and 0 <= dx < 6:
                if board[dy][dx] == target and check[dy][dx] == 0:
                    check[dy][dx] = 1
                    q.append((dy, dx))
                    boom.append((dy, dx))
    if len(boom) >= 4: # 연결된 게 4개 이상이면
        for y, x in boom:
            board[y][x] = '.' #터트리기
        return 1
    return 0

color = []
board = []

for _ in range(12):
    board.append(list(input()))
ans = 0

while True:
    turn = 0
    for y in range(12):
        for x in range(6):
            if board[y][x] != '.':
                turn += BFS(y, x)
    if turn == 0:
        print(ans)
        break
    else:
        ans += 1
    gravity() # 턴 한 번 돌고 밑으로 떨어트리기