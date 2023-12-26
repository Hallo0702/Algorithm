from collections import defaultdict, deque
N = int(input())
order = defaultdict(list)
time = [0] * (N+1)
cnt = [0] * (N+1)
answer = [0] * (N+1)
queue = deque()

for i in range(1,N+1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]

    for j in range(1,len(lst)-1):
        order[lst[j]].append(i)
        cnt[i] += 1

    if cnt[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer[now] += time[now]

    for next in order[now]:
        answer[next] = max(answer[next],answer[now])
        cnt[next] -= 1
        if cnt[next] == 0:
            queue.append(next)

for i in range(1,N+1):
    print(answer[i])
