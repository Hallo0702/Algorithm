import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    T, S = map(int, input().split())
    arr.append((T,S))

arr.sort(key=lambda x:-x[1])

answer = sys.maxsize
for i in range(N):
    T, S = arr[i]
    if answer > S:
        answer = S

    answer -= T

print(max(answer,-1))