N = int(input())

answer = 0

while N > 0:
    N = N // 5
    answer += N

print(answer)