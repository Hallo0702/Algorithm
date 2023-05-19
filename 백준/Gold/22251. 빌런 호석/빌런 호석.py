# N은 최대 수, K는 최대 자리수, P 반전시킬 LED 수, X 현재 멈춘 층수
N, K, P, X = map(int, input().split())


numbers = {
    0 : 0b1110111,
    1 : 0b0010010,
    2 : 0b1011101,
    3 : 0b1011011,
    4 : 0b0111010,
    5 : 0b1101011,
    6 : 0b1101111,
    7 : 0b1010010,
    8 : 0b1111111,
    9 : 0b1111011
}

check = [[0 for _ in range(10)] for _ in range(10)]


for i in range(10):
    for j in range(10):
        num = numbers[i] ^ numbers[j]
        while num != 0:
            if num % 2 == 1:
                check[i][j] += 1
            num = num >> 1

str_X = str(X)
while len(str_X) < K:
    str_X = '0' + str_X


def dfs(level, cnt, now):
    if level >= len(now):
        if int(now) == X:
            return 0
        if int(now) <= N and int(now) >= 1:
            return 1
        return 0

    total = 0

    save = now[level]
    for i in range(10):
        if check[int(now[level])][i] <= cnt:
            temp = list(now)
            temp[level] = str(i)
            temp = ''.join(temp)
            total += dfs(level+1,cnt-check[int(save)][i],temp)
            
    return total


answer = dfs(0,P,str_X)
print(answer)