bracket = input()
stack = []
answer = 0
res = 1

for i in range(len(bracket)):

    if bracket[i] == '(':
        res *= 2
        stack.append('(')

    elif bracket[i] == '[':
        res *= 3
        stack.append('[')

    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break

        if bracket[i-1] == '(':
            answer += res

        res //= 2
        stack.pop()

    elif bracket[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break

        if bracket[i-1] == '[':
            answer += res

        res //= 3
        stack.pop()

if stack:
    answer = 0

print(answer)