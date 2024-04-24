import sys
input = sys.stdin.readline
from collections import deque

s, t = map(int, input().split())
q = deque()
visit = set()

if s == t:
    print(0)
else:
    answer = -1

    q.append((s,''))
    visit.add(s)

    while q:
        x, word = q.popleft()

        if x == t:
            answer = word
            break

        mul_x = x * x
        if 0 < mul_x <= 10 ** 9 and mul_x not in visit:
            q.append((mul_x,word+'*'))
            visit.add(mul_x)

        plus_x = x + x
        if 0 < plus_x <= 10 ** 9 and plus_x not in visit:
            q.append((plus_x,word+'+'))
            visit.add(plus_x)

        dev_x = x / x
        if dev_x not in visit:
            q.append((dev_x,word+'/'))
            visit.add(dev_x)


    print(answer)