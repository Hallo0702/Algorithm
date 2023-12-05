s,N,K,R1,R2,C1,C2 = map(int, input().split()) # 시간, 크기, 검정되는 크기, 좌표들

def check(num, x, y):
    black = num // N
    blank = (N-K)//2
    # 전체의 가운데 안에 있나? 그렇다면 1
    if num == 1:
        return 0

    if black * blank <= x < num - (black * blank) and black * blank <= y < num - (black * blank):
        return 1
    else:
        return check(black,x%black,y%black)

if s == 0:
    print(0)
else:
    for i in range(R1,R2+1):
        for j in range(C1,C2+1):
            cnt = N ** s
            print(check(cnt,i,j),end='')
        print()
