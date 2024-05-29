import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
for idx in range(len(arr)):

    num = arr[idx]

    while q and q[-1][1] >= num:
        q.pop()

    while q and q[0][0] <= idx - L:
        q.popleft()

    q.append((idx,num))

    print(q[0][1],end=' ')