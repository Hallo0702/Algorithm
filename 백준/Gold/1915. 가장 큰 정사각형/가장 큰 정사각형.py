n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
answer = 0

for i in range(n):
    if arr[i][0] == 1:
        answer = 1

for i in range(m):
    if arr[0][i] == 1:
        answer = 1


for i in range(1,n):
    for j in range(1,m):

        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j],arr[i][j-1],arr[i-1][j-1]) + 1
            if answer < arr[i][j]:
                answer = arr[i][j]

print(answer**2)