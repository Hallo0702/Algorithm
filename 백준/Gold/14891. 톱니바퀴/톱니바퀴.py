from collections import deque

gear = []

for _ in range(4):
    gear.append(deque(map(int, list(input()))))

K = int(input())


def turn(gear_num, dir):
    rotate_gear = gear_num
    rotate_dir = dir

    rotate_gear -= 1
    rotate_dir *= -1

    while rotate_gear >= 0:
        if gear[rotate_gear][2] == gear[rotate_gear + 1][6]:
            break

        rotate_gear -= 1

    for i in range(gear_num-1,rotate_gear,-1):
        gear[i].rotate(rotate_dir)
        rotate_dir *= -1

    rotate_gear = gear_num + 1
    rotate_dir = dir * -1

    while rotate_gear < 4:
        if gear[rotate_gear][6] == gear[rotate_gear - 1][2]:
            break

        rotate_gear += 1

    for i in range(gear_num + 1, rotate_gear):
        gear[i].rotate(rotate_dir)
        rotate_dir *= -1

    gear[gear_num].rotate(dir)


for k in range(K):
    number , d = map(int, input().split())
    turn(number-1, d)


answer = 0
for i in range(4):
    answer += gear[i][0] * (2**i)

print(answer)