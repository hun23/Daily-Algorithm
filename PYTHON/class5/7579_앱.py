N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
apps = [(0, 0)] + [(costs[i], memories[i]) for i in range(N)]
# knapsack?
apps.sort()
dp = [0] * (M + 1)

for i in range(1, N + 1):
    for j in range(M, apps[i][0] -1, -1):
        dp[j] = max(dp[j], dp[j - apps[i][1]] + apps[i][0])
print(dp)