import heapq

def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key= lambda x:(x[0],x[1]))
    q = []
    
    end = 0
    taken_time = 0
    for i in range(len(jobs)):
        request, taken = jobs[i]
        
        if request < end:
            heapq.heappush(q,(taken,request))
        elif request == end:
            heapq.heappush(q,(taken,request))
            while q and end <= request:
                time_taken, start_time = heapq.heappop(q)
                end = max(end+time_taken, start_time+time_taken)
                taken_time += end - start_time
        else:
            while q and end <= request:
                time_taken, start_time = heapq.heappop(q)
                end = max(end+time_taken, start_time+time_taken)
                taken_time += end - start_time
            heapq.heappush(q,(taken,request))
    
    while q:
        time_taken, start_time = heapq.heappop(q)
        end = max(end+time_taken, start_time+time_taken)
        taken_time += end - start_time
    
    answer = taken_time // len(jobs)
            
    
    return answer