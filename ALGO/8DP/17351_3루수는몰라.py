from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def up(r, c, char):
    global arr
    if r - 1 >= 0 and arr[r - 1][c] == char:
        return True
    return False

def left(r, c, char):
    global arr
    if c - 1 >= 0 and arr[r][c - 1] == char:
        return True
    return False

N = int(input())
arr = [input().strip() for _ in range(N)]

if N <= 2:
    print(0)
    exit()

# r, c까지 왔을 때 최대 MOLA 개수
dp = [[0] * N for _ in range(N)]
# 구하기
for i in range(N * N):
    r, c = divmod(i, N)
    val_up = dp[r - 1][c] if r - 1 >= 0 else 0
    val_left = dp[r][c - 1] if c - 1 >= 0 else 0
    ok_up, ok_left = False, False
    if arr[r][c] == "A":
        if up(r, c, "L"):
            if up(r - 1, c, "O"):
                if up(r - 2, c, "M") or left(r - 2, c, "M"):
                    ok_up = True
            if left(r - 1, c, "O"):
                if up(r - 1, c - 1, "M") or left(r - 1, c - 1, "M"):
                    ok_up = True
        if left(r, c, "L"):
            if up(r, c - 1, "O"):
                if up(r - 1, c - 1, "M") or left(r - 1, c - 1, "M"):
                    ok_left = True
            if left(r, c - 1, "O"):
                if up(r, c - 2, "M") or left(r, c - 2, "M"):
                    ok_left = True
    val_up += (1 if ok_up else 0)
    val_left += (1 if ok_left else 0)
    dp[r][c] = max(val_up, val_left)
print(dp[N - 1][N - 1])
