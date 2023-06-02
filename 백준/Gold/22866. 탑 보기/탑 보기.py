N = int(input())
L = list(map(int, input().split()))


stack = []
result = [0 for _ in range(N)]
near = [[100001,100001] for _ in range(N)]

for idx, h in enumerate(L):

    while stack and h >= stack[-1][1]:
        stack.pop()

    result[idx] += len(stack)

    if len(stack) > 0:
        d = abs(idx - stack[-1][0])
        if d < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = d
    stack.append((idx, h))

stack = []
for idx, h in reversed(list(enumerate(L))):

    while stack and h >= stack[-1][1]:
        stack.pop()

    result[idx] += len(stack)

    if len(stack) > 0:
        d = abs(idx - stack[-1][0])
        if d < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = d
    stack.append((idx, h))

for i in range(N):
    if result[i] == 0:
        print(0)
    else:
        print(result[i],near[i][0]+1)
