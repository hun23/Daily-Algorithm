from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for m in range(1, N + 1):
        prefix_sum[n][m] = (
            arr[n - 1][m - 1]
            + prefix_sum[n - 1][m]
            + prefix_sum[n][m - 1]
            - prefix_sum[n - 1][m - 1]
        )
for x1, y1, x2, y2 in queries:
    temp = (
        prefix_sum[x2][y2]
        - prefix_sum[x2][y1 - 1]
        - prefix_sum[x1 - 1][y2]
        + prefix_sum[x1 - 1][y1 - 1]
    )
    println(temp)
