N, K = map(int, input().split())
array = list(input())

answer = 0

for i in range(N):
    if array[i] == 'P':
        for j in range(max(0,i-K),min(N,i+K+1)):
            if array[j] == 'H':
                answer += 1
                array[j] = 'E'
                break

print(answer)



