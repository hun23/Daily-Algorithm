a, b, n, w = map(int, input().split())
ans = []

for num_goat in range(1, n):
    if a * (n - num_goat) + b * num_goat == w:
        ans.append((n - num_goat, num_goat))
if len(ans) != 1:
    print(-1)
else:
    print(*ans[0])
