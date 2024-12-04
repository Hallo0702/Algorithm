def break_puyo():
    global flag
    visit = [[0]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if not visit[i][j] and puyo[i][j] != '.':
                visit[i][j] = 1
                q = [(i,j)]
                waiting = [(i,j)]

                while q:
                    x, y = q.pop()
                    for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny] and puyo[nx][ny] == puyo[x][y]:
                            visit[nx][ny] = 1
                            q.append((nx,ny))
                            waiting.append((nx,ny))

                if len(waiting) >= 4:
                    flag = 1
                    for i, j in waiting:
                        puyo[i][j] = '.'


def down_puyo():
    for j in range(6):
        for i in range(11,-1,-1):
            if puyo[i][j] == '.':
                bot = i
                break
        else:
            continue

        for i in range(bot-1,-1,-1):
            if puyo[i][j] != '.':
                puyo[bot][j], puyo[i][j] = puyo[i][j], puyo[bot][j]
                bot -= 1



puyo = [list(input()) for _ in range(12)]
answer = 0
flag = 1
while flag:
    flag = 0
    break_puyo()
    if flag:
        answer += 1
        down_puyo()
print(answer)
