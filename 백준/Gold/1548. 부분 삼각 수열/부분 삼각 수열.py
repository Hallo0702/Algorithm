def solve():
    N = int(input())

    arr = sorted(list(map(int,input().split())))

    if N <= 2:
        return N

    answer = 2

    start = 0
    end = 2

    while N - start > answer:
        if arr[start] + arr[start+1] > arr[end]:
            answer = max(answer,end-start+1)
            end += 1
        else:
            start += 1
            end = start+2

    return answer


print(solve())