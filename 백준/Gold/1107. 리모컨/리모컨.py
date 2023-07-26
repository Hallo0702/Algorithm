N = int(input())
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []

l = len(str(N))

result = abs(N - 100)

for i in range(min(10**(l+2),1000000)):

    numbers = str(i)

    for num in numbers:
        if num in broken:
            break
    else:
        result = min(result, abs(N-i)+len(numbers))


print(result)