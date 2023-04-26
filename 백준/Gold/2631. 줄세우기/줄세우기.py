N = int(input())
arr = [0]
for i in range(N):
    arr.append(int(input()))
DP = [0]*(N+1)
for i in range(1,N+1):
    for j in range(0,i):
        if arr[i] > arr[j] and DP[i] <= DP[j]:
            DP[i] = DP[j] + 1
print(N-max(DP))