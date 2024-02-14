from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


# def recur(idx):
#     global N
#     if idx > N:
#         return -(1000 * 1_500_000)
#     if idx == N:
#         return 0
#     if dp[idx] != -1:
#         return dp[idx]
#     ret = max(recur(idx + 1), recur(idx + arr[idx][0]) + arr[idx][1])
#     dp[idx] = ret
#     return ret


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
# print(recur(0))
for i in range(N - 1, -1, -1):
    if i + arr[i][0] > N:  # 당일 일 불가
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + arr[i][0]] + arr[i][1], dp[i + 1])
print(dp[0])
