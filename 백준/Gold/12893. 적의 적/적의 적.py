from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


q = deque()
team = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if team[i] == 0:
        q.append(i)
        team[i] = 1
        while q:
            flag = 1
            num = q.popleft()

            for number in graph[num]:
                if team[number] == team[num]:
                    print(0)
                    exit(0)
                elif team[number] == 0:
                    team[number] = team[num] * -1
                    q.append(number)

else:
    print(1)
