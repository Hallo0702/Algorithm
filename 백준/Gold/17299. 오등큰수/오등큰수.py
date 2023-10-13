import sys
from collections import defaultdict

def ngf():
    input = sys.stdin.readline

    N = int(input())
    arr = list(map(int, input().split()))
    F = [0] * 1000001
    for i in range(N):
        F[arr[i]] += 1

    stack = []
    answer = [-1] * N

    for i in range(N):
        while stack and F[arr[stack[-1]]] < F[arr[i]]:
            answer[stack.pop()] = arr[i]

        stack.append(i)

    print(*answer)

ngf()