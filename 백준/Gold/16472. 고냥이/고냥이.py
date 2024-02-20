N = int(input())
S = input()
word = {}

answer = 0
left = 0
for i in range(len(S)):

    if S[i] in word:
        word[S[i]] += 1
    else:
        word[S[i]] = 1
        while len(word) > N:
            word[S[left]] -= 1
            if word[S[left]] == 0:
                del word[S[left]]
            left += 1

    answer = max(answer, i - left + 1)
print(answer)