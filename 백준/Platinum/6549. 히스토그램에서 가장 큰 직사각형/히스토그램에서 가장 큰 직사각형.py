while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    n = arr.pop(0)

    answer = arr[0]

    st = []

    for i in range(n):
        if len(st) == 0:
            st.append((arr[i],0, i))
            continue

        if arr[i] > st[-1][0]:
            st.append((arr[i],st[-1][2] + 1, i))
        elif arr[i] == st[-1][0]:
            st.append((arr[i], st[-1][1], i))

        else:

            while st:
                if st[-1][0] > arr[i]:
                    h, idx, origin = st.pop()
                    tmp = h * (i - idx)
                    if tmp > answer:
                        answer = tmp
                else:
                    break

            if len(st) == 0:
                st.append((arr[i],0,i))
            else:
                if st[-1][0] == arr[i]:
                    st.append((arr[i], st[-1][1], i))
                else:
                    st.append((arr[i], st[-1][2] + 1, i))

    while st:
        h, idx, origin = st.pop()
        tmp = h * (n - idx)

        if tmp > answer:
            answer = tmp

    print(answer)

