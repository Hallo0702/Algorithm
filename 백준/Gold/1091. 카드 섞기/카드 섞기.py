N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))


def check(arr):

    for i in range(len(arr)):
        if arr[i] != (i % 3):
            return False
    else:
        return True


def change(arr):

    res = []
    for i in range(len(arr)):
        res.append(arr[S[i]])

    return res


answer = 0
result = []
for i in range(N):
    result.append(i%3)

while 1:

    if result == P:
        break

    result = change(result)
    answer += 1

    if check(result):
        answer = -1
        break

print(answer)