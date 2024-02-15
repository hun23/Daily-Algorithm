import random
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(100000)
input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(N, K, items, idx, weight):
    if idx > N or weight > K:
        return -(100_000 * 101)
    if idx == N:
        return 0

    ret = max(
        recur(N, K, items, idx + 1, weight),
        recur(N, K, items, idx + 1, weight + items[idx][0]) + items[idx][1],
    )
    return ret


def s2(N, K, items):
    # i번째 아이템까지 고르고 무게가 W인 경우 최대 V를 저장
    dp = [[-1] * (K + 1) for _ in range(N)]
    # print(recur(0, 0))
    if items[0][0] <= K:
        dp[0][items[0][0]] = items[0][1]
    dp[0][0] = 0
    for i in range(1, N):
        for j in range(K + 1):
            if dp[i - 1][j] == -1:
                continue
            # i번째 아이템을 고른 경우
            if j + items[i][0] <= K:
                dp[i][j + items[i][0]] = max(
                    dp[i][j + items[i][0]], dp[i - 1][j] + items[i][1]
                )
            # i번째 아이템을 고르지 않은 경우
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    return max(dp[-1])


for t in range(10):
    N, K = random.randint(1, 10), random.randint(1, 100_000)
    items = [
        tuple((random.randint(1, 100_000), random.randint(0, 1000))) for _ in range(N)
    ]
    a, b = recur(N, K, items, 0, 0), s2(N, K, items)
    if a != b:
        print("=" * 100)
        print(a, b)
        print(N, K, items)
