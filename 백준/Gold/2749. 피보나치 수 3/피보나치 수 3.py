# 피사노 주기

n = int(input())

mod = 1000000
before = 0
after = 1
p = 15 * (mod//10)

n = n % p
for i in range(2,n+1):
    before, after = after, (before + after) % mod

print(after)