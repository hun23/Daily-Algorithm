from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
if N == 1:
    print(1)
    exit()
# i만큼 채우는 경우의 수
dp = [-1] * (N + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007
print(dp[-1])
