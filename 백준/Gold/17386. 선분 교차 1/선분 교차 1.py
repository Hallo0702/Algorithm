x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def func(a1,b1,a2,b2,a3,b3):
    return a1*b2+a2*b3+a3*b1-a2*b1-a3*b2-a1*b3

A = func(x1,y1,x2,y2,x3,y3)
B = func(x1,y1,x2,y2,x4,y4)
C = func(x3,y3,x4,y4,x1,y1)
D = func(x3,y3,x4,y4,x2,y2)

answer = 1 if A*B < 0 and C*D < 0 else 0
print(answer)