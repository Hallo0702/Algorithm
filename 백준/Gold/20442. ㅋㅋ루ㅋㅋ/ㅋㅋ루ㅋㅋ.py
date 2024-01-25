KKRKK = input()

cnt = 0
for i in range(len(KKRKK)):
    if KKRKK[i] == 'R':
        cnt += 1

left_k, right_k = 0, 0
left, right = 0, len(KKRKK)-1
answer = cnt

while cnt > 0:

    while cnt and KKRKK[left] == 'K':
        left += 1
        left_k += 1

    while cnt and KKRKK[right] == 'K':
        right -= 1
        right_k += 1

    answer = max(answer, cnt + 2*min(left_k,right_k))

    if left_k > right_k:
        right -= 1
        cnt -= 1
    elif left_k < right_k:
        left += 1
        cnt -= 1
    else:
        left += 1
        right -= 1
        cnt -= 2

print(answer)