N = int(input())
arr = [0]*(N+1)
arr[0] = 1
if N % 2 == 1:
    print(arr[N])
else:
    arr[2] = 3
    if N > 3:
        for i in range(4,N+1,2):
            arr[i] += arr[i-2]*3
            for j in range(i-4,-1,-2):
                arr[i] += arr[j]*2
    print(arr[N])
