KKRKK = input()

cnt = 0
for i in range(len(KKRKK)):
    if KKRKK[i] == 'R':
        cnt += 1

left_k, right_k = 0, 0
left, right = 0, len(KKRKK)-1
answer = 0
while left <= right:

    if KKRKK[left] == 'R' and KKRKK[right] == 'R':
        answer = max(answer, cnt+2*min(left_k,right_k))
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
        continue

    if KKRKK[left] == 'K':
        left += 1
        left_k += 1

    if KKRKK[right] == 'K':
        right -= 1
        right_k += 1

print(answer)
