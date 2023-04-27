word = input()
target = input()


def pos(now, end):

    if len(end) == len(now):
        if end == now:
            return 1
        else:
            return 0

    if now[-1] == 'A':
        flag = pos(now[:-1], end)
        if flag == 1:
            return 1

    if now[0] == 'B':
        flag = pos(now[-1:0:-1],end)
        if flag == 1:
            return 1

    return 0


answer = pos(target, word)
print(answer)