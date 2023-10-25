def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 1
    end = distance
    
    while start <= end:
        middle = (start+end) // 2
        cnt = 0
        now = 0
        for i in range(len(rocks)):
            if rocks[i] < now + middle:
                cnt += 1
                if cnt > n:
                    break
            else:
                now = rocks[i]
        
        if cnt > n:
            end = middle-1
        else:
            start = middle+1
            answer = middle

    return answer