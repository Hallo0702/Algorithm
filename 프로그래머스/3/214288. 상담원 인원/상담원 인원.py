from itertools import product
import heapq

def find_waiting_time(w_list, num):
    cnt = 0
    result = 0
    end = []
    for s, e in w_list:
        while end and s >= end[0]:
            heapq.heappop(end)
            cnt -= 1

        if cnt < num:
            heapq.heappush(end,s+e)
            cnt += 1

        else:
            result += end[0] - s
            heapq.heappush(end, e + end[0])
            heapq.heappop(end)


    return result


def solution(k, n, reqs):
    waiting_list = [[] for _ in range(k + 1)]
    wating_time = [[0 for _ in range(n+1)] for _ in range(k + 1)]

    for req in reqs:
        waiting_list[req[2]].append((req[0], req[1]))

    for i in range(1, k + 1):
        for j in range(1, n+1):
            wating_time[i][j] = find_waiting_time(waiting_list[i], j)

    result = [0] + [1] * k
    number = n - k
    while number > 0:
        max_reduce_time = 0
        max_reduce_time_type = 0

        for t in range(1,k+1):
            now_time = wating_time[t][result[t]]
            next_time = wating_time[t][result[t]+1]

            reduce_time = now_time - next_time
            if max_reduce_time <= reduce_time:
                max_reduce_time = reduce_time
                max_reduce_time_type = t

        if max_reduce_time == 0:
            break

        result[max_reduce_time_type] += 1
        number -= 1

    answer = 0
    for i in range(1,k+1):
        answer += wating_time[i][result[i]]
    return answer

print(solution(2,3,[[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))