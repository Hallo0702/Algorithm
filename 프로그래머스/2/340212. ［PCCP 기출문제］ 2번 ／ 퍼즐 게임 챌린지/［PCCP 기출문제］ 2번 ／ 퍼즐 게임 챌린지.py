def solution(diffs, times, limit):
    n = len(diffs)
    answer = 0
    
    def cal_time(level):
    
        result = 0
        for i in range(n):
            if diffs[i] <= level:
                result += times[i]
            else:
                result += (times[i]+times[i-1])*(diffs[i]-level) + times[i]
        
            if result > limit:
                break
        return result
    
    
    left = 1
    right = max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        res = cal_time(mid)
        if res <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer