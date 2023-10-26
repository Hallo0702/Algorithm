import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
li = [0, L] + list(map(int, input().split()))
li.sort()

# m을 최대로 휴게소를 세울 수 있나
# 이분탐색의 시작과 끝을 고속도로의 시작과 끝으로 설정
# 휴게소 사이에 새로운 휴게소를 지을때 특정 거리(m)로 지었을때의 휴게소 갯수를 count
# start지점과 end지점이 교차될 때가 가장 최대값이므로 이때의 mid값을 출력한다.
st, en = 1, li[-1]
while st <= en:
    cnt = 0
    m = (st + en) // 2                              # (같은 간격)
    for i in range(1, len(li)):                     # m 간격보다 큰 간격인 거리에 휴게소를 설치했을 때 설치 가능한 개수를 변수 cnt에 저장
        if (li[i] - li[i - 1]) > m:
            cnt += (li[i] - li[i - 1] - 1) // m     # 이미 지어진 자리에는 지을 수 없기 때문에 -1

    if cnt > M:
        st = m + 1      # 설치된 휴게소의 개수가 M보다 크면 휴게소 설치 간격을 늘리고
    else:
        en = m - 1
        ans = m         # 설치된 휴게소의 개수가 M보다 작으면 휴게소 설치 간격을 줄인다


print(ans)