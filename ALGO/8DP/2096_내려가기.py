from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
funcs = [max, min]
for condition in range(2):
    dp = [0, 0, 0]
    func = funcs[condition]
    # 초기값
    for i in range(3):
        dp[i] = arr[0][i]

    for i in range(1, N):
        left_temp = func(dp[0], dp[1])
        right_temp = func(dp[1], dp[2])
        dp[0] = left_temp + arr[i][0]
        dp[1] = func(left_temp, right_temp) + arr[i][1]
        dp[2] = right_temp + arr[i][2]
    ans[condition] = func(dp)
print(*ans)
