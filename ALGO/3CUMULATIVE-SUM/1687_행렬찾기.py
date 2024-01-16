from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, M = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().strip())))
println(arr)
prefix_row = [[0] * (M + 1) for _ in range(N + 1)]
prefix_col = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        if arr[n - 1][m - 1] == 0:
            prefix_row[n][m] = prefix_row[n - 1][m] + 1
            prefix_col[n][m] = prefix_col[n][m - 1] + 1
        else:
            prefix_row[n][m] = 0
            prefix_col[n][m] = 0
for r in prefix_row:
    println(r)
println("="*10)
for c in prefix_col:
    println(c)

ans = 0
for n in range(1, N + 1):
    for m in range(1, M + 1):
        temp = prefix_row[n][m] * prefix_col[n][m]
        if ans < temp:
            ans = temp
println(ans)
