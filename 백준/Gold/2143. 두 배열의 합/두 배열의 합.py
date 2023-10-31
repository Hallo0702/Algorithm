T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

Adict = {}
Bdict = {}

for n in range(N):
    s = 0
    for i in range(n,N):
        s += A[i]
        if s in Adict:
            Adict[s] += 1
        else:
            Adict[s] = 1

for m in range(M):
    s = 0
    for i in range(m,M):
        s += B[i]
        if s in Bdict:
            Bdict[s] += 1
        else:
            Bdict[s] = 1

answer = 0

for a in Adict:
    if Bdict.get(T-a):
        answer += Adict[a] * Bdict[T-a]

print(answer)