import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(input().strip())

    arr.sort()

    for j in range(n-1):
        if arr[j+1].startswith(arr[j]):
            print("NO")
            break
    else:
        print("YES")