N = int(input())

if N == 1:
    print(0)
else:
    prime = [0,0] + [1] * (N-1)
    prime_num = []
    for i in range(2,N+1):
        if prime[i]:
            prime_num.append(i)
            for j in range(2*i,N+1,i):
                prime[j] = 0

    answer = 0
    left = 0
    right = 0
    total = 2

    while left <= right:
        if total > N:
            total -= prime_num[left]
            left += 1
        else:
            if total == N:
                answer += 1
            right += 1
            if right == len(prime_num):
                break
            total += prime_num[right]

    print(answer)