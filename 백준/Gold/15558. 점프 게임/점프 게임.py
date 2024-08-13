import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())


left = list(map(int,str(input().rstrip())))
right = list(map(int,str(input().rstrip())))
visit = [[0,0] for _ in range(N)]
q = deque()
q.append((0,0,0)) # 시간, 방향(l==0,r==1), 위치
visit[0][0] = 1

while q:

    time, direct, number = q.popleft()
    if number + 1 >= N or number + K >= N:
        print(1)
        break

    if direct == 0:
        if left[number+1] == 1 and visit[number+1][0] == 0: # 앞칸이 존재하는 경우 전진
            q.append((time+1,0,number+1))
            visit[number+1][0] = 1
        if time+1 <= number-1 and left[number-1] == 1 and visit[number-1][0] == 0: # 뒤칸이 존재하는 경우 후진
            q.append((time+1,0,number-1))
            visit[number-1][0] = 1
        if right[number + K] == 1 and visit[number+K][1] == 0:
            q.append((time+1,1,number+K))
            visit[number+K][1] = 1
    else:
        if right[number + 1] == 1 and visit[number+1][1] == 0:
            q.append((time + 1, 1, number + 1))
            visit[number+1][1] = 1
        if time + 1 <= number-1 and right[number - 1] == 1 and visit[number-1][1] == 0:
            q.append((time + 1, 1, number - 1))
            visit[number-1][1] = 1
        if left[number + K] == 1 and visit[number+K][0] == 0:
            q.append((time + 1, 0, number + K))
            visit[number+K][0] = 1

else:
    print(0)


