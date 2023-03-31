import sys

N, M = map(int, sys.stdin.readline().split())
# left & right padding
arr = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# get cumsum
# each row first
for r in range(N + 1):
    for c in range(1, N + 1):
        arr[r][c] += arr[r][c - 1]
# each column
for c in range(N + 1):
    for r in range(1, N + 1):
        arr[r][c] += arr[r - 1][c]
# for a in arr:
#     print(a)

# solve
for m in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x), sys.stdin.readline().split())
    big, left_column, upper_row, small = arr[x2][y2], arr[x2][y1 - 1], arr[x1 - 1][y2], arr[x1 - 1][y1 - 1]
    answer = big - left_column - upper_row + small
    print(answer)
