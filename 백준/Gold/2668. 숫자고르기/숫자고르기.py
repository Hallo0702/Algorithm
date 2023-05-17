N = int(input())

arr = [0]
selected = [0] * (N+1)

for i in range(N):
    arr.append(int(input()))

for i in range(1,N+1):
    if selected[i] == 0 and selected[arr[i]] == 0:
        selected_idx = selected[:]
        selected_numbers = selected[:]

        now = i
        next = arr[i]

        while 1:
            if selected_idx[now] == 0:
                selected_idx[now] = 1
                selected_numbers[next] = 1

                now, next = next, arr[next]
            else:
                break

        if selected_idx == selected_numbers:
            selected = selected_idx[:]

print(sum(selected))
for i in range(1,N+1):
    if selected[i] == 1:
        print(i)