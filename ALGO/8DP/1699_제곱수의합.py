from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(100000)
input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
# i를 만드는데 필요한 최소 제곱수 항
dp = [100_001] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    j = 1
    while i - j * j >= 0:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1
print(dp[-1])
