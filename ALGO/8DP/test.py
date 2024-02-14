import random
from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def s1(N, arr):
    dp = [[1001] * 3 for _ in range(N)]  # i 인덱스를 r, g, b 색으로 칠하는 최소비용

    # 초기값 설정
    for i in range(3):
        dp[0][i] = arr[0][i]

    for i in range(1, N):
        for color in range(3):  # i 인덱스를 color로 칠하려면
            temp = 1001 * N
            for prev_color in range(3):
                if color == prev_color:  # 이전과 다른 색으로 칠한 비용
                    continue
                temp = min(temp, dp[i - 1][prev_color])  # 중 최소
            temp += arr[i][color]  # 더하기 i 인덱스를 color로 칠하는데 필요한 비용
            dp[i][color] = temp
    return min(dp[-1])


def s2(N, RGBs):
    dp = [[0] * 3 for _ in range(N)]
    for color in range(3):
        dp[N - 1][color] = RGBs[N - 1][color]
    for n in range(N - 1 - 1, -1, -1):
        for i in range(3):
            temp = 2147483647
            for j in range(3):
                if i != j:
                    temp = min(temp, RGBs[n][i] + dp[n + 1][j])
            dp[n][i] = temp
    return min(dp[0])


for t in range(100):
    N = random.randint(2, 1000)
    arr = [[random.randint(1, 1000) for _ in range(3)] for _ in range(N)]
    a, b = s1(N, arr), s2(N, arr)
    if a != b:
        print("=" * 100)
        print(a, b)
        print(N, arr)
