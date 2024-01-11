from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")

def update(origin, add):
    for key, val in add.items():
        origin[key] = origin.get(key, 0) + val
    return origin

def diff(origin, dif):
    for key, val in dif.items():
        origin[key] = origin.get(key, 0) - val
    return origin

N = int(input())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

cnts = dict()
prefix_sum = [[dict()] * (N + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, N + 1):
        temp = {arr[r][c]: 1}
        temp = update(temp, prefix_sum[r - 1][c])
        temp = update(temp, prefix_sum[r][c - 1])
        temp = diff(temp, prefix_sum[r - 1][c - 1])
        prefix_sum[r][c] = temp

for x1, y1, x2, y2 in queries:
    big = dict(prefix_sum[x2][y2])
    left = prefix_sum[x2][y1 - 1]
    up = prefix_sum[x1 - 1][y2]
    left_up = prefix_sum[x1 - 1][y1 - 1]
    big = diff(big, left)
    big = diff(big, up)
    big = update(big, left_up)
    ans = 0
    for key, val in big.items():
        if val > 0:
            ans += 1
    println(ans)
