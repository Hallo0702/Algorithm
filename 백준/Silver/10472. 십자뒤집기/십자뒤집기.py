from collections import deque

P = int(input())
bit = ["110100000","111010000","011001000","100110100","010111010","001011001","000100110","000010111","000001011"]



for p in range(P):
    target = ''
    for i in range(3):
        word = input()
        for w in word:
            if w == '*':
                target += '1'
            else:
                target += '0'

    target_number = int(target, 2)

    visit = [-1 for _ in range(512)]
    q = deque()
    q.append(0)
    visit[0] = 0


    while (q and visit[target_number] == -1):
        now = q.popleft()
        if now == target_number:
            break

        for b in bit:
            next = now ^ int(b, 2)

            if visit[next] == -1:
                visit[next] = visit[now] + 1
                q.append(next)


    print(visit[target_number])
