import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M == 0:
    print(N)
else:

    room = [i for i in range(N+1)]

    broken_wall = sorted([tuple(map(int, input().split())) for _ in range(M)],key=lambda x : x[0])

    max_y = 0

    for x, y in broken_wall:
        if y <= max_y:
            continue
        for i in range(max(x,max_y)+1,y+1):
            room[i] = room[x]
        max_y = y

    answer = len(set(room)) - 1
    print(answer)
