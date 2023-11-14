import sys
input = sys.stdin.readline

N = int(input())

flowers = []

for i in range(N):
    b_m,b_d, w_m,w_d = map(int, input().split())
    flowers.append([100*b_m + b_d , 100*w_m+w_d])

flowers.sort()

last_day = 301
last = 0
answer = 0

while flowers:

    if last_day >= 1201 or last_day < flowers[0][0]:
        break

    for i in range(len(flowers)):
        if last_day >= flowers[0][0]:
            if last <= flowers[0][1]:
                last = flowers[0][1]

            flowers.remove(flowers[0])

        else:
            break

    last_day = last
    answer += 1


if last_day < 1201:
    print(0)
else:
    print(answer)