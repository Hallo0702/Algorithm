def isPal(word):
    if word == word[::-1]:
        return True
        

def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPal(s[i:j]):
                answer = max(answer,j-i)
    

    return answer