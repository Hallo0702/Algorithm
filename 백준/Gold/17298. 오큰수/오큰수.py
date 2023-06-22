N = int(input())
arr = [0] + list(map(int, input().split()))
nge = [-1] * (N+1)
stack = []
for i in range(1,N+1):
    if len(stack) == 0:
        stack.append(i)
    else:
        while len(stack) != 0:
            x = stack[-1]
            if arr[i] > arr[x]:
                stack.pop()
                nge[x] = arr[i]
            else:
                stack.append(i)
                break
        else:
            stack.append(i)
for i in range(1,N+1):
    print(nge[i],end=' ')