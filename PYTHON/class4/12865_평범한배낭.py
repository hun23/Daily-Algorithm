N, K = map(int, input().split())
items = []
for n in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
items.sort()
# combinations of weights -> N
# dp[N] = set
dp = [0] * (N + 1)
for n in range(items[0][0], N + 1):
    # dp[n] =
    pass