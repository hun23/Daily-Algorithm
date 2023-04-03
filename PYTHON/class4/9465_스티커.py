T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(3)]
    # for a in arr:
    #     print(a)
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = 0
    for n in range(1, N):
        dp[0][n] = arr[0][n] + max(dp[1][n - 1], dp[2][n - 1])
        dp[1][n] = arr[1][n] + max(dp[0][n - 1], dp[2][n - 1])
        dp[2][n] = 0 + max(dp[0][n - 1], dp[1][n - 1])
    # for d in dp:
    #     print(d)
    print(max(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))