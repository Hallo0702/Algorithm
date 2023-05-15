N = int(input())

switch = list(map(int,list(input())))
target = list(map(int,list(input())))


def turn_switch(S,T,C):
    temp = S[:]
    cnt = C
    for i in range(1,N):
        if temp[i-1] == target[i-1]:
            continue

        cnt += 1

        for j in range(i-1,min(i+2,N)):
            temp[j] = 1 - temp[j]

    if temp == T:
        return cnt
    else:
        return -1


result1 = turn_switch(switch,target,0)

switch[0] = 1 - switch[0]
switch[1] = 1 - switch[1]

result2 = turn_switch(switch,target,1)

if result1 != -1 and result2 != -1:
    print(min(result1,result2))
else:
    print(max(result1,result2))

