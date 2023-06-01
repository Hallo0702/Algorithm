N, M, L, K = map(int, input().split())
stars = []
answer = K
# 별 입력받음
for _ in range(K):
    stars.append(list(map(int, input().split())))

# 전체 좌표를 돌면 시간초과날게 당연해보이므로 k개의 별좌표를 기준으로 돌아야할듯
# 별 두개를 기준으로 잡고 A별의 X좌표, B별의 Y좌표를 기준으로 트램펄린을 놓는다고 치고 그 안에 들어가는 별의 개수를 세봄

# A별 i
max_cnt = 0
for i in range(K):
    # B별 j
    for j in range(K):
        # 그 안에 들어가는 별 개수 확인
        cnt = 0
        for k in range(K):
            if stars[i][0] <= stars[k][0] <= stars[i][0] + L and stars[j][1] <= stars[k][1] <= stars[j][1] + L:
                cnt += 1

        max_cnt = max(max_cnt,cnt)

print(answer-max_cnt)