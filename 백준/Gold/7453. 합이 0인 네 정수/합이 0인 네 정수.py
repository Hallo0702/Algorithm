import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(sorted,zip(*arr)))

AB = []
CD = []

for i in range(N):
    for j in range(N):
        AB.append(arr[0][i] + arr[1][j])
        CD.append(arr[2][i] + arr[3][j])


AB.sort()
CD.sort()

left = 0
right = len(CD)-1
answer = 0

while left < len(AB) and right >= 0:

    if AB[left] + CD[right] < 0:
        left += 1

    elif AB[left] + CD[right] > 0:
        right -= 1

    else:
        left_c = 1
        right_c = 1
        while left < len(AB)-1 and AB[left] == AB[left+1]:
            left_c += 1
            left += 1
        while right > 0 and CD[right] == CD[right-1]:
            right_c += 1
            right -= 1
        answer += left_c * right_c
        left += 1
        right -= 1

print(answer)