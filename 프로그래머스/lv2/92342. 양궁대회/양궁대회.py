def dfs(now,cnt,arrow,info):
    global Max,Max_list,num
    
    if cnt == 0:
        score = 0
        for i in range(11):
            if arrow[i] > info[i]:
                score += 10 - i
            else:
                if info[i] != 0:
                    score -= 10 - i
                    
        if score > 0:
            print(score)
            if score > Max:
                Max = score
                Max_list = []
                for i in range(11):
                    Max_list.append(arrow[i])
            elif score == Max:
                for i in range(10,0,-1):
                    if arrow[i] > Max_list[i]:
                        Max_list = []
                        for i in range(11):
                            Max_list.append(arrow[i])
                    elif arrow[i] < Max_list[i]:
                        return
        
        return
    
    if now == 10:
        next_arrow = arrow
        next_arrow[10] = cnt
        dfs(now+1,0,next_arrow,info)
        next_arrow[10] = 0
        return
    
    elif now < 10: 
        next_arrow = arrow

        next_arrow[now] = cnt
        dfs(now+1,0,next_arrow,info)
        next_arrow[now] = 0

        if cnt > info[now]+1:
            next_arrow[now] = info[now]+1
            dfs(now+1,cnt-(info[now]+1),next_arrow,info)
            next_arrow[now] = 0

        next_arrow[now] = 0
        dfs(now+1,cnt,next_arrow,info)
    
    
    


def solution(n, info):
    global Max_list,Max,num
    answer = []
    Max_list= [-1]
    Max = 0
    num = n
    dfs(0,n,[0]*11,info)
    answer = Max_list
    return answer