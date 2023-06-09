A, B = map(int, input().split())

cnt = len(bin(B))-2

psum = [0] * (cnt+1)

for i in range(1,cnt+1):
    psum[i] = 2 ** (i-1) + 2 * psum[i-1]


def count_sum(num):
    if num == 0:
        return 0
    length = len(bin(num))-2
    count = psum[length-1] + (num - 2**(length-1) +1) + count_sum(num - 2**(length-1))
    return count


print(count_sum(B)-count_sum(A-1))