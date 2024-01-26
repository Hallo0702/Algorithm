N = int(input())

if N == 1:
    print(0)
else:
    prime = [1] * (N+1)
    for i in range(3,int(N**0.5)+1,2):
        if prime[i]:
            for j in range(2*i,N+1,i):
                prime[j] = 0
    prime_num = [2] + [i for i in range(3,N+1,2) if prime[i]]

    answer = 0
    left = 0
    total = 0

    for p in prime_num:
        total += p

        while total > N:
            total -= prime_num[left]
            left += 1

        if total == N:
            answer += 1
            total -= prime_num[left]
            left += 1

    print(answer)