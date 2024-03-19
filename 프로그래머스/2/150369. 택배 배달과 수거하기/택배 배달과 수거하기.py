def solution(cap, n, deliveries, pickups):
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    
    deliver = 0
    pickup = 0
    
    answer = 0
    
    for i in range(n,0,-1):
        deliver += deliveries[i]
        pickup += pickups[i]
        
        while deliver > 0 or pickup > 0:
            answer += 2 * i
            deliver -= cap
            pickup -= cap
        
    return answer