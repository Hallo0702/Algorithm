N = int(input())

height = list(map(int, input().split()))

answer = 0

for idx_x, height_x in enumerate(height):
    cnt = 0
    max_right_slope = None

    for idx_y in range(idx_x+1, N):
        height_y = height[idx_y]
        right_slope = (height_y - height_x) / (idx_y - idx_x)
        if max_right_slope == None or max_right_slope < right_slope:
            max_right_slope = right_slope
            cnt += 1

    min_left_slope = None

    for idx_y in range(idx_x-1,-1,-1):
        height_y = height[idx_y]
        left_slope = (height_y - height_x) / (idx_y - idx_x)
        if min_left_slope == None or min_left_slope > left_slope:
            min_left_slope = left_slope
            cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)