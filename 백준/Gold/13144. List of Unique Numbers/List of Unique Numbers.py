from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = 0

cnt = defaultdict(int)

answer = 0


while end < N and start < N:

    if cnt[arr[end]] == 0:
        cnt[arr[end]] += 1
        end += 1
        answer += end - start

    else:
        while cnt[arr[end]] > 0:
            cnt[arr[start]] -= 1
            start += 1

print(answer)