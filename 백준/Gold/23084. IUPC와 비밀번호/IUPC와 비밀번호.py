import sys
input = sys.stdin.readline
S = input().rstrip()
max_cnt = [0] * 26

for i in range(len(S)):
    max_cnt[ord(S[i])-ord('a')] += 1

N = int(input())
for n in range(N):
    word = input().rstrip()

    if len(word) < len(S):
        print("NO")
        continue

    word_cnt = [0] * 26
    extra = 0


    left = 0
    right = len(S)-1
    for i in range(right+1):
        num = ord(word[i])-ord('a')
        word_cnt[num] += 1
        if max_cnt[num] < word_cnt[num]:
            extra += 1


    if len(word) == len(S) and extra == 1:
        print('YES')
        continue

    if len(word) > len(S) and extra <= 1:
        print('YES')
        continue

    while right < len(word)-1:

        left_num = ord(word[left])-ord('a')
        word_cnt[left_num] -= 1
        if word_cnt[left_num] >= max_cnt[left_num]:
            extra -= 1
        right_num = ord(word[right+1])-ord('a')
        word_cnt[right_num] += 1
        if word_cnt[right_num] > max_cnt[right_num]:
            extra += 1

        if extra <= 1:
            print('YES')
            break

        left += 1
        right += 1

    else:
        print('NO')

