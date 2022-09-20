from collections import defaultdict 
import math

def solution(fees, records):
    answer = []
    
    dict = {}
    total = defaultdict(int)
    
    for record in records :
        time, number, state = record.split()
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time
    
    last_time = 23 * 60 + 59
    for car, time in dict.items():
        total[car] += last_time - time
    
    for car, time in total.items():
        cost = fees[1]
        if time > fees[0]:
            cost += fees[3] * math.ceil((time - fees[0])/fees[2])
        
        answer.append([car,cost])
    
    answer.sort(key = lambda x: x[0])
    
    
    
    return [fee[1] for fee in answer]