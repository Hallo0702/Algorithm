import heapq
from collections import deque


gu = list(input())
N = len(gu)
cube = list(input())

gu.sort()
cube.sort()

gu = deque(gu[:(N+1)//2])
cube = deque(cube[((N+1)//2):])


answer = ['?' for _ in range(N)]
flag = 0
front = 0
back = N-1
while front <= back:
    if flag == 0:
        if cube and gu[0] >= cube[-1]:
            answer[back] = gu.pop()
            back -= 1
        else:
            answer[front] = gu.popleft()
            front += 1

        flag = 1

    elif flag == 1:
        if gu and cube[-1] <= gu[0]:
            answer[back] = cube.popleft()
            back -= 1
        else:
            answer[front] = cube.pop()
            front += 1

        flag = 0


answer = "".join(answer)
print(answer)