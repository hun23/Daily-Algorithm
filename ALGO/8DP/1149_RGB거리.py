from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[1001] * 3 for _ in range(N)]  # i 인덱스를 r, g, b 색으로 칠하는 최소비용

# 초기값 설정
for i in range(3):
    dp[0][i] = arr[0][i]

for i in range(1, N):
    for color in range(3):  # i 인덱스를 color로 칠하려면
        temp = 1001 * N  # 최대비용 1000 + 1을 N번 칠하는 값(이론상 불가능한 값)
        for prev_color in range(3):
            if color == prev_color:  # 이전과 다른 색으로 칠한 비용
                continue
            temp = min(temp, dp[i - 1][prev_color])  # 중 최소
        temp += arr[i][color]  # 더하기 i 인덱스를 color로 칠하는데 필요한 비용
        dp[i][color] = temp
print(min(dp[-1]))
