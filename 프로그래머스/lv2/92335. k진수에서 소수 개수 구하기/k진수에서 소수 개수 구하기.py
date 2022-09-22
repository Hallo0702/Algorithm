import math

def NtoK(N, K):
    k_word = []
    while N:
        N, w = N // K, N % K
        k_word.append(str(w))
    k_word.reverse()
    k_word = "".join(k_word)
    return k_word


def is_prime(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    elif number % 2 == 0:
        return 0
    
    for num in range(3,math.ceil(number**(1/2))+1,2):
        if number % num == 0:
            return 0
    
    return 1
    
    

        
def solution(n, k):
    answer = 0
    k_word = NtoK(n, k)
    words = k_word.split("0")
    remove = {""}
    words = [word for word in words if word not in remove]
    words = list(map(int, words))

    for word in words:
        answer += is_prime(word)
    
    return answer