from collections import defaultdict

M, N = map(int, input().split())

multiverse = defaultdict(int)

for _ in range(M):
    universe = list(map(int, input().split()))
    sorted_universe = sorted(list(set(universe)))

    order = {}
    for idx in range(len(sorted_universe)):
        order[sorted_universe[idx]] = idx

    universe_order = tuple([order[i] for i in universe])

    multiverse[universe_order] += 1

answer = 0

for cnt in multiverse.values():
    answer += (cnt * (cnt - 1)) // 2

print(answer)
