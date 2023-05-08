n, m = map(int, input().split())
arr = list(map(int, input().split()))
st=0
ed=m-1
max_st=arr[st]
max_ed=arr[ed]
ans=0

while st < ed:
    max_st=max(max_st, arr[st])
    max_ed=max(max_ed, arr[ed])
    if max_st>=max_ed:
        ans += max_ed-arr[ed]
        ed -= 1
    elif max_st<max_ed:
        ans += max_st-arr[st]
        st += 1
print(ans)