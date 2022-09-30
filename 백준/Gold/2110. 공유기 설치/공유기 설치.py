N,C = map(int, input().split()) # 집의개수 공유기의 개수
arr = [] # 집의 위치(거리)
for i in range(N):
    arr.append(int(input()))
# 가장 짧은 공유기 사이의 거리가 최대가 되어야 함.
# 가장 짧은 공유기 사이의 거리를 찾아보자
arr.sort() # 집 거리순으로 정렬
start = 1 # 거리의 최소단위
end = arr[-1] - arr[0] # 가장 긴 거리

while start <= end: # 평범한 이분 탐색
    m = (start+end)//2 # m을 가장 짧은 공유기 사이의 거리라 하자
    first = arr[0] # 우선 1번집에 공유기 설치
    cnt = 1 # 설치된 공유기 수
    for i in range(1,N):
            if arr[i] >= first+m: # 그전 설치된 집에서 m이상 떨어져 있으면 집에 설치하고 cnt 증가
                cnt += 1
                first = arr[i] # 설치된 집으로 first 변경

    if cnt < C: # 설치된 공유기 수가 설치해야하는 공유기 수보다 적으면 거리를 줄여야함
        end = m-1
    else:
        start = m+1 # 설치된 공유기 수가 많거나 같으면 거리를 늘려봄.
print(end) # end의 위치가 최댓값이됨.
