import sys
input = sys.stdin.readline
inf = sys.maxsize

def cal(w1,w2,n):
    cnt = 0
    for i in range(n):
        if w1[i] != w2[i]:
           cnt += 1
    return cnt

S = " " + input().rstrip()
N = int(input())
words = [input().rstrip() for _ in range(N)]
DP = [[inf for _ in range(len(S))] for _ in range(len(S))]
DP[0][0] = 0

for i in range(1,len(S)+1):
    if DP[i-1][0] == inf:
        continue
    for word in words:
        l = len(word)
        if sorted(S[i:i+l]) == sorted(word):
            DP[i][i+l-1] = min(DP[i][i+l-1],DP[i-1][0]+cal(S[i:i+l],word,l))
            DP[i+l-1][0] = min(DP[i+l-1][0],DP[i][i+l-1])

if DP[-1][0] != inf:
    print(DP[-1][0])
else:
    print(-1)