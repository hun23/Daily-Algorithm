# backtracking - Timeout
# def backtasking(N, RGBs, idx, color_before, cost):
#     global answer
#     if idx == N:
#         if cost < answer:
#             answer = cost
#         return
#     elif cost >= answer:
#         return
#
#     for color in range(3):
#         if color == color_before:
#             continue
#         solve(N, RGBs, idx + 1, color, cost + RGBs[idx][color])
#
# DP?
# def dp(idx, used, last_color):
#     global N, RGBs, memo
#     if idx == N:
#         return 0
#
#     if memo[used]:  # DP
#         return memo[used]
#
#     save = 2147483647
#     for i in range(3):
#         if last_color == i:
#             continue
#         save = min(save, RGBs[idx][i] + dp(idx + 1, used + (3 ** idx) * i, i))
#     memo[used] = save
#     return memo[used]


N = int(input())
RGBs = list()
for n in range(N):
    RGBs.append(list(map(int, input().split())))
answer = 2147483647
# backtasking(N, RGBs, idx=0, color_before=-1, cost=0)
# memo = [0] * (3**N)
# dp(0, 0, -1)
# print(memo[0])
dp = [[0] * 3 for _ in range(N)]  # dp[n][i] -> min value when nth row's color i is selected
for color in range(3):
    dp[N - 1][color] = RGBs[N - 1][color]  # last row of dp == RGBs' last row

for n in range(N-1 - 1, -1, -1):  # fill dp from N-2 to 0
    for i in range(3):  # for 3 colors at row n
        temp = 2147483647
        for j in range(3):  # for 3 color at row n+1, i!=j
            if i != j:
                temp = min(temp, RGBs[n][i] + dp[n + 1][j])
        dp[n][i] = temp  # save min value
# for p in dp:
#     print(p)
print(min(dp[0]))
