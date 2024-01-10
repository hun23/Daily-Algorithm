N = int(input())
guards = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for n in range(N):
    covered = [0 for _ in range(1000)]
    for i, (start, end) in enumerate(guards):
        if n == i:
            continue
        covered[start:end] = [1] * (end - start)
    ans = max(ans, sum(covered))
print(ans)