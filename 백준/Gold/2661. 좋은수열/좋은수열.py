N = int(input())


def check(sequence):

    for i in range(1,len(sequence)+1//2):
        if sequence[-i::] == sequence[-(2*i):-i]:
            return False
    else:
        return True


def dfs(seq): # 맨 앞자리에서 부터 시작

    if len(seq) == N:
        return seq

    for number in ['1','2','3']: # 123 순서대로 확인
        if check(seq+number):
            ans = dfs(seq+number)
            if ans != '':
                return ans

    return ''


print(dfs(''))