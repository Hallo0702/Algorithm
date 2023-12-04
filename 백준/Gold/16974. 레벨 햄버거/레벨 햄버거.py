N,X = map(int, input().split())
patty = [1] * (N+1)
layer = [1] * (N+1)

for i in range(1,N+1):
    layer[i] = layer[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1


def eat(n,x):
    if n == 0:
        return 1

    if x == 1:
        return 0
    elif x == layer[n-1] + 2:
        return patty[n-1] + 1
    elif x < layer[n-1] + 2:
        return eat(n-1,x-1)
    elif x < layer[n]:
        return patty[n-1] + 1 + eat(n-1,x-(layer[n-1]+2))
    else:
        return patty[n]

print(eat(N,X))

