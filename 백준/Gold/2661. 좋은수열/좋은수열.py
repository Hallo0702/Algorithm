N = int(input())


def check(sequence):

    for i in range(1,len(sequence)+1//2):
        if sequence[-i::] == sequence[-(2*i):-i]:
            return False
    else:
        return True


def dfs(seq): # 맨 앞자리에서 부터 시작

    if len(seq) == N:
        print(seq)
        exit()

    for number in ['1','2','3']: # 123 순서대로 확인
        if check(seq+number):
            dfs(seq+number)

    return


dfs('')