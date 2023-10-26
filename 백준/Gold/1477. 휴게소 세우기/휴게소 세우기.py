N,M,L = map(int,input().split())
road = [0,L] + list(map(int,input().split()))
road.sort()

st, ed = 1, L
answer = 0

while st <= ed:
    cnt = 0
    mid = (st + ed) // 2
    for i in range(len(road)-1):
        if road[i+1] - road[i] > mid:
            cnt += (road[i+1] - road[i] -1) // mid

    if cnt > M:
        st = mid + 1
    else:
        ed = mid - 1
        answer = mid

print(answer)
