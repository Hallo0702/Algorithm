S = input()
T = input()

while T:
    if T[-1] == 'A':
        T = T[0:-1]
    elif T[-1] == 'B':
        T = T[0:-1]
        T = T[::-1]

    if S == T:
        print(1)
        break
else:
    print(0)
