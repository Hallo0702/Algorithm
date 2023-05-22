word = input()
boom = input()
boom_length = len(boom)

stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == boom[-1] and ''.join(stack[-boom_length:]) == boom:
        for j in range(boom_length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
