from copy import deepcopy

N, M, K = map(int, input().split())
arr2 = list(list(map(int, input().split())) for i in range(N))
operation = []
num = []
for i in range(K):
    operation.append(list(map(int,input().split())))
    num.append(i)
num_turn = []
min = 5001
check = [False]*K

def turn(arr,r,c,s): # r세로, c가로 , s 칸수 (문제는 1,1부터 시작이므로 넣을때 -1-1해줘야함)
    if s == 0:
        result = arr
        return result
    else:
        tmp = arr[r-s][c-s]
        t = 2*s
        for i in range(t): #아래부터 정렬
            arr[r-s+i][c-s] = arr[r-s+i+1][c-s]
        for i in range(t):
            arr[r+s][c-s+i] = arr[r+s][c-s+i+1]
        for i in range(t):
            arr[r+s-i][c+s] = arr[r+s-i-1][c+s]
        for i in range(t):
            arr[r-s][c+s-i] = arr[r-s][c+s-i-1]
        arr[r-s][c-s+1] = tmp
        result = turn(arr,r,c,s-1)
        return result

def per(level):
    if level == K:
        arr = deepcopy(arr2)
        for n in num_turn:
            arr = turn(arr,operation[n][0]-1,operation[n][1]-1,operation[n][2])
        global min
        for i in range(N):
            total = 0
            for j in range(M):
                total += arr[i][j]
            if total < min:
                min = total
        return
    else:
        for i in range(K):
            if check[i] == False:
                num_turn.append(num[i])
                check[i] = True
                per(level+1)
                check[i] = False
                num_turn.pop()

per(0)
print(min)