word = input()
wordType = [0 for _ in range(len(word))]
LFlag = 0
for i in range(len(word)):
    if word[i] == '_':
        wordType[i] = -1

    elif word[i] in ['A','E','I','O','U']:
        wordType[i] = 1
    elif word[i] == 'L':
        LFlag = 1
    else:
        wordType[i] = 0

answer = 0

def check_pos(numbers):

    for i in range(2,len(wordType)):
        num = numbers[i-2] + numbers[i-1] + numbers[i]
        if num == 3 or num == 0:
            return 0

    return 1

def find_funny(idx,cnt,flag):
    global answer

    for i in range(idx,len(wordType)):

        if wordType[i] == -1:
            wordType[i] = 1
            find_funny(i+1,cnt*5,flag)
            wordType[i] = 0
            find_funny(i+1,cnt*20,flag)
            find_funny(i+1,cnt,1)
            wordType[i] = -1
            break

    else:
        if flag == 1 and check_pos(wordType):
            answer += cnt

find_funny(0,1,LFlag)
print(answer)