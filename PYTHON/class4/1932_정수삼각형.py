N = int(input())
arr = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for n in range(N):
    for i, num in enumerate(input().split()):
        arr[n][i] = int(num)

# fill last row
for n in range(N):
    dp[N - 1][n] = arr[N - 1][n]
# fill rest
for r in range(N-1 -1, -1, -1):
    for c in range(r + 1):
        temp = 0
        for i in range(2):
            temp = max(temp, arr[r][c] + dp[r + 1][c + i])
        dp[r][c] = temp
print(dp[0][0])