from itertools import combinations

def Manhattan(idx1,idx2):
    return abs(idx1[0]-idx2[0]) + abs(idx1[1]-idx2[1])

def solution(places):
    answer = []
    for restroom in places:
        
        people = []
        for i in range(5):
            for j in range(5):
                if restroom[i][j] == 'P':
                    people.append((i,j))
        
        for p1, p2 in combinations(people,2):
            M = Manhattan(p1,p2)
            if M < 2:
                answer.append(0)
                break
            elif M == 2:
                if p1[0] == p2[0]:
                    if restroom[p1[0]][p1[1]+1] == 'O':
                        answer.append(0)
                        break
                elif p1[0]+1 == p2[0]:
                    if restroom[p1[0]][p2[1]] == 'O' or restroom[p2[0]][p1[1]] == 'O':
                        answer.append(0)
                        break
                else:
                    if restroom[p1[0]+1][p1[1]] == 'O':
                        answer.append(0)
                        break
        else:
            answer.append(1)
                        
        
        
    return answer