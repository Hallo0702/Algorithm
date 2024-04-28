N = int(input())
arr = list(map(int, input().split()))

LIS = [0]
for i in range(N):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
    else:
        start = 0
        end = len(LIS)

        while start < end:
            mid = (start+end)//2

            if LIS[mid] >= arr[i]:
                end = mid # mid -1 이 아닌 이유는 같은경우 그 자리로 옮겨야 할 수도 있기 떄문
            else:
                start = mid+1
        LIS[end] = arr[i]
print(len(LIS)-1)