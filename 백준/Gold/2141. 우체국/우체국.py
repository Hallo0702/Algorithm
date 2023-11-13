import sys
input = sys.stdin.readline

N = int(input())
X = []
total = 0
for i in range(N):
    a, b = map(int,input().split())
    X.append((a,b))
    total += b

X.sort(key= lambda x:x[0])

people = 0
for i in range(N):
    people += X[i][1]
    if people >= total / 2:
        print(X[i][0])
        break
