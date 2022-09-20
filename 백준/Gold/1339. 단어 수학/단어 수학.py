# 10! -> 모든 경우 고려
N = int(input())
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
words = []
word_dicts = {}
answer = 0


# 주어진 단어를 words에 입력
for _ in range(N):
    words.append(input())


# 필요한 알파벳 추출해서 딕셔너리에 입력
for word in words:
    LEN = len(word) - 1

    for alpha in word:
        if alpha in word_dicts:
            word_dicts[alpha] += 10 ** LEN
        else:
            word_dicts[alpha] = 10 ** LEN

        LEN -= 1


# sorted => list 반환
word_dicts = sorted(word_dicts.values(), reverse=True)


# 정렬 되어 나온 큰 값부터 9, 8, 7, 6 ... 0 할당
MAX = 9
for value in word_dicts:
    answer += value * MAX
    MAX -= 1


print(answer)