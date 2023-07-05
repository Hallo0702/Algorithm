N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()


for i in range(N):

    if books[i] > 0:
        idx = i
        break
else:
    idx = N

answer = 0
for i in range(0,idx,M):
    answer += abs(books[i]) * 2
for i in range(N-1,idx-1,-M):
    answer += abs(books[i]) * 2

print(answer-max(abs(books[0]),abs(books[-1])))
