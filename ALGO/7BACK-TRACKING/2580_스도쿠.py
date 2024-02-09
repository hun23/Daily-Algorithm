from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")


def possible(idx, num):
    r, c = idx // 9, idx % 9
    base_r, base_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(9):
        if board[i][c] == num \
            or board[r][i] == num \
            or board[base_r + i // 3][base_c + i % 3] == num:
            return False
    return True


def recur(idx):
    global board
    r, c = idx // 9, idx % 9
    if idx == 81:
        for b in board:
            print(*b)
        exit()
    if board[r][c] != 0:
        recur(idx + 1)
        return
    for i in range(1, 10):
        if possible(idx, i):
            board[r][c] = i
            recur(idx + 1)
            board[r][c] = 0
    return

board = [list(map(int, input().split())) for _ in range(9)]
recur(0)
