import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
    
q = deque()

for idx in range(len(A)):

    while q and q[-1][0] >= A[idx]:
        q.pop()

    q.append((A[idx],idx))

    if q[0][1] <= idx - L:
        q.popleft()

    print(q[0][0],end=' ')