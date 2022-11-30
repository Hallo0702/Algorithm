def solution(n, k, cmd):
    kakao_dict = {}
    delete_stack = []
    
    check = ['O'] * n
    
    now = k
    
    kakao_dict[0] = [0,1]
    kakao_dict[n-1] = [n-2,n-1]
    for i in range(1,n-1):
        kakao_dict[i] = [i-1,i+1]
    
    for c in cmd:
        if len(c) >= 3:
            order, number = c.split(" ")
        else:
            order = c[0]
        
        if order == "U":
            for _ in range(int(number)):
                now = kakao_dict[now][0]
        
        elif order == "D":
            for _ in range(int(number)):
                now = kakao_dict[now][1]
        
        elif order == "C":
            delete_stack.append(now)
            check[now] = 'X'
            pre, next = kakao_dict[now]
            if now == kakao_dict[now][0]:
                kakao_dict[kakao_dict[now][1]][0] = kakao_dict[now][1]
                now = kakao_dict[now][1]
            elif now == kakao_dict[now][1]:
                kakao_dict[kakao_dict[now][0]][1] = kakao_dict[now][0]
                now = kakao_dict[now][0]
            else:
                kakao_dict[kakao_dict[now][1]][0] = kakao_dict[now][0]
                kakao_dict[kakao_dict[now][0]][1] = kakao_dict[now][1]
                now = kakao_dict[now][1]
        elif order == "Z":
            deleted = delete_stack.pop()
            check[deleted] = 'O'
            if deleted == kakao_dict[deleted][0]:
                kakao_dict[kakao_dict[deleted][1]][0] = deleted
            elif deleted == kakao_dict[deleted][1]:
                kakao_dict[kakao_dict[deleted][0]][1] = deleted
            else:
                kakao_dict[kakao_dict[deleted][1]][0] = deleted
                kakao_dict[kakao_dict[deleted][0]][1] = deleted
                

    
    answer = ''.join(check)
            
    return answer