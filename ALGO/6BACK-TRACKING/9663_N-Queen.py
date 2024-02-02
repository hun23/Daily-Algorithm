from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def possible(row, col):
    global N, queens, used
    if used["column"][col]:
        return False
    if used["right_diagonal"][(N - col) + row]:
        return False
    if used["left_diagonal"][col + row]:
        return False
    return True


def update(row, col, put):
    global used
    used["column"][col] = put
    used["right_diagonal"][(N - col) + row] = put
    used["left_diagonal"][col + row] = put


def recur(row):
    global N, queens
    if row == N:
        return 1
    ret = 0
    for col in range(N):
        if possible(row, col):
            queens[row] = col
            update(row, col, True)
            ret += recur(row + 1)
            update(row, col, False)
    return ret


N = int(input())
queens = [-1] * N
used = {
    "column": [False] * N,
    "right_diagonal": [False] * (2 * N + 1),
    "left_diagonal": [False] * (2 * N + 1),
}
print(recur(0))
