N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for number in arr:
    if number <= answer + 1:
        answer += number
    else:
        break

print(answer + 1)