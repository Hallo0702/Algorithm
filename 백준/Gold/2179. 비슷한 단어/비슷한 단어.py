from collections import defaultdict

N = int(input())

word_dict = []
word_idx = {}
word_cnt = [0] * (N)

answer = 0

def find(s, t):
    cnt = 0
    for i in range(min(len(s),len(t))):
        if s[i] == t[i]:
            cnt += 1
        else:
            break

    return cnt


for i in range(N):
    word = input()
    word_dict.append(word)
    if word not in word_idx:
        word_idx[word] = i

sorted_word_dict = sorted(list(set(word_dict)))

for i in range(len(sorted_word_dict)-1):
    result = find(sorted_word_dict[i],sorted_word_dict[i+1])
    idx_a = word_idx[sorted_word_dict[i]]
    idx_b = word_idx[sorted_word_dict[i+1]]

    word_cnt[idx_a] = max(word_cnt[idx_a],result)
    word_cnt[idx_b] = max(word_cnt[idx_b], result)

max_cnt = max(word_cnt)

pre = 0
for i in range(N):
    if pre == 0:
        if word_cnt[i] == max_cnt:
            print(word_dict[i])
            pre = word_dict[i][:max_cnt]
    else:
        if word_cnt[i] == max_cnt and word_dict[i][:max_cnt] == pre:
            print(word_dict[i])
            break