N, A, B = map(int, input().split())

if A + B > N + 1:
    print(-1)
else:
    answer = []
    for i in range(1,A):
        answer.append(i)
    answer.append(max(A,B))
    for i in range(B-1,0,-1):
        answer.append(i)

    print(answer[0],end=' ')
    for i in range(N-len(answer)):
        print(1, end=' ')
    for i in range(1,len(answer)):
        print(answer[i], end=' ')