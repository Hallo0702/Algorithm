import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    if K < 5:
        return 0

    if K == 26:
        return N

    words = []
    for _ in range(N):
        words.append(set(input().rstrip()))

    study = [0] * 26
    for w in ('a','n','t','i','c'):
        study[ord(w)-ord('a')] = 1

    global answer
    answer = 0

    def dfs(level, cnt):
        global answer

        if cnt == K-5:
            result = 0
            for word in words:
                for w in word:
                    if study[ord(w)-ord('a')] == 0:
                        break
                else:
                    result += 1

            answer = max(answer,result)
            return

        for i in range(level, 26):
            if study[i] == 0:
                study[i] = 1
                dfs(i,cnt+1)
                study[i] = 0

    dfs(0,0)
    return answer

print(solve())



