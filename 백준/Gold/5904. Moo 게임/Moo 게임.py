N = int(input())

num = 0
Snum = 3

while N > Snum:
    num += 1
    Snum = (Snum * 2) + (num+3)

num -= 1
Snum = (Snum - (num+3)) // 2

while num >= -1:
    if N == Snum+1:
        print("m")
        break
    elif N > Snum+1 and N <= Snum+(num+4):
        print("o")
        break
    elif N <= Snum:
        num -= 1
        Snum = (Snum - (num+3)) // 2
    else:
        N -= Snum + (num + 4)
        num -= 1
        Snum = (Snum - (num + 3)) // 2
