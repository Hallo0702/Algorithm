import sys
input = sys.stdin.readline

N = int(input().rstrip())
users = []
for i in range(N):
    users.append(input().rstrip())

count = dict()
pre = set()
for user in users:
    if user in count:
        count[user] += 1
        print(user + str(count[user]))
    else:
        count[user] = 1
        result = ''
        flag = 0
        for c in user:
            result += c
            if result not in pre and flag == 0:
                print(result)
                flag = 1
            pre.add(result)

        if flag == 0:
            print(result)
