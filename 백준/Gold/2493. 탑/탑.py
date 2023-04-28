N = int(input())
tower = list(map(int, input().split()))
stack = []

for idx in range(N):
    height = tower[idx]
    while stack and stack[-1][1] < height:
        stack.pop()

    if len(stack) == 0:
        print(0,end=' ')
        stack.append((idx+1,height))
    else:
        print(stack[-1][0],end=' ')
        stack.append((idx+1,height))
