from collections import deque

R, C = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(input()))

q = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'F':
            q.append((-1,i,j))

        elif arr[i][j] == 'J':
            j_x = i
            j_y = j

q.append((0,j_x,j_y))

dy = [-1,0,1,0]
dx = [0,1,0,-1]
answer = "IMPOSSIBLE"

while q:
    time, x, y = q.popleft()

    if time > -1 and (x == 0 or y == 0 or x == R-1 or y == C-1):
        answer = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != '#':
            if time == -1 and arr[nx][ny] != 'F':
                arr[nx][ny] = 'F'
                q.append((-1,nx,ny))

            elif time > -1 and arr[nx][ny] == '.':
                arr[nx][ny] = 'J'
                q.append((time+1,nx,ny))

print(answer)