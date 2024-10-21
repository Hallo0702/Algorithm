N = int(input())
arr = list(map(int, list(input() for _ in range(N))))

cum = [0 for _ in range(2 * N + 1)]

for i in range(2 * N):
    cum[i+1] = cum[i] + arr[i % N]

answer = 0
total, right = cum[N], 1

for left in range(N):
    while right < 2 * N + 1 and cum[right] - cum[left] <= total - (cum[right] - cum[left]):
        answer = max(answer, cum[right] - cum[left])
        right += 1
print(answer)

