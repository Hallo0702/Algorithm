import sys
input = sys.stdin.readline
N, T = map(int, input().split())
arr = [0] * (100001)
psum = [0] * (100001)
max_time = 0
for n in range(N):
    K = int(input().rstrip())
    for k in range(K):
        start, end = map(int, input().split())
        if max_time < end:
            max_time = end
        arr[start] += 1
        arr[end] -= 1


for i in range(1,100001):
    arr[i] += arr[i-1]

psum[0] = arr[0]
for i in range(1,max_time):
    psum[i] = psum[i-1] + arr[i]

answer_s = 0
answer_e = T
answer = psum[T-1]
for i in range(T,max_time):
    if psum[i] - psum[i-T] > answer:
        answer_e = i+1
        answer_s = i-T+1
        answer = psum[i] - psum[i-T]

print(answer_s,answer_e)
