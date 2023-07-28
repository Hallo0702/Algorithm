N = int(input())

eggs = [] # 내구도, 무게

for i in range(N):
    eggs.append(list(map(int, input().split())))

answer = 0


def dfs(level, egg):

    global answer

    if level == N:
        result = 0
        for i in range(N):
            if egg[i][0] <= 0:
                result += 1
        answer = max(answer, result)
        return

    if egg[level][0] <= 0:
        dfs(level+1,egg)

    else:
        key = 0
        for i in range(N):
            if i != level and egg[i][0] > 0:
                key = 1
                egg[level][0] -= egg[i][1]
                egg[i][0] -= egg[level][1]
                dfs(level+1,egg)
                egg[level][0] += egg[i][1]
                egg[i][0] += egg[level][1]

        if not key:
            dfs(level+1,egg)



dfs(0,eggs)
print(answer)

