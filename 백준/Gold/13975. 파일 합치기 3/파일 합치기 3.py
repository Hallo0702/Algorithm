import heapq
import sys
input = sys.stdin.readline

# 시간이 너무 오래걸려 찾던중 다른 풀이법 참고
T = int(input())

for t in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    filesCnt = dict()
    q = []

    for i in range(K):
        if files[i] == 0:
            if 0 in filesCnt: # 0은 1개만 있으면 몇개가있든 비용이 0이기 때문에 1개만 넣습니다. 여러개를 넣으면 오히려 시간만 더듬
                continue

        if files[i] in filesCnt:
            filesCnt[files[i]] += 1
        else:
            filesCnt[files[i]] = 1
            heapq.heappush(q,files[i])

    answer = 0
    while len(q) > 1 or (len(q) == 1 and filesCnt[q[0]] > 1):
        fileCnt = filesCnt[q[0]] # 가장 작은 값의 개수 체크

        if fileCnt == 1: # 1개일때 다음것과 합침
            del filesCnt[q[0]]
            num1 = heapq.heappop(q)
            num2 = q[0]

            answer += num1 + num2
            if num1 + num2 not in filesCnt:
                filesCnt[num1+num2] = 0
                heapq.heappush(q,num1+num2)
            filesCnt[num1 + num2] += 1

            if filesCnt[num2] == 1:
                del filesCnt[num2]
                heapq.heappop(q)
            else:
                filesCnt[num2] -= 1

        else: # 2개 이상일 때 한번에 작동
            num1 = q[0]
            answer += 2 * num1 * (fileCnt // 2)
            if 2 * num1 not in filesCnt: # 딕셔너리에 더한값이 있다면 +fileCnt//2 없다면 추가
                filesCnt[2 * num1] = 0
                heapq.heappush(q,2 * num1)
            filesCnt[2 * num1] += (fileCnt // 2)

            if fileCnt % 2 == 0: # 짝수라면 전부 제거
                del filesCnt[q[0]]
                heapq.heappop(q)
            else: # 홀수라면 1개만 남기고 제거
                filesCnt[q[0]] = 1
    print(answer)



'''
## 기존 간단한 풀이법
import heapq
import sys
input = sys.stdin.readline


T = int(input())

for t in range(T):
    K = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)

    answer = 0

    for _ in range(K-1):
        num1 = heapq.heappop(q)
        num2 = heapq.heappop(q)

        answer += num1 + num2

        heapq.heappush(q,num1+num2)

    print(answer)

'''