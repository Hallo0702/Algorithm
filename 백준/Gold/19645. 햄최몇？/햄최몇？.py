N = int(input())
hamburger = list(map(int, input().split()))

s = set([])
s.add((0,0))

for i in range(N):
    ham = hamburger[i]
    s_list = list(s)
    for x, y in s_list:
        if (x+ham,y) not in s:
            s.add((x+ham, y))
        if (x, y+ham) not in s:
            s.add((x, y+ham))

total = sum(hamburger)
answer = 0

s_list = list(s)
for x, y in s_list:
    gilone = total - x - y
    if gilone <= x and gilone <= y:
        answer = max(gilone,answer)

print(answer)