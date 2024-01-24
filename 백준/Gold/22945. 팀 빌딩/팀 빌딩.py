import sys
input = sys.stdin.readline

N = int(input())
developers = list(map(int, input().split()))
answer = 0

left, right = 0, N-1

while left < right:
    answer = max(answer, (right-left-1)*min(developers[left],developers[right]))

    if developers[left] > developers[right]:
        right -= 1
    else:
        left += 1

print(answer)