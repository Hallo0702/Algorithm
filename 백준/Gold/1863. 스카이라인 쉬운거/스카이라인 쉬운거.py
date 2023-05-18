N = int(input())

sky = []
answer = 0

for i in range(N):
    idx, height = map(int, input().split())

    while sky:
        if sky[-1] > height:
            sky.pop()
            answer += 1
        else:
            break

    if (len(sky) == 0 or sky[-1] < height) and height != 0:
        sky.append(height)


if sky:
    answer += len(sky)

print(answer)