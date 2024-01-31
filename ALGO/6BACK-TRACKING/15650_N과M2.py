from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, start):
    global N, M, arr
    if idx == M:
        print(*arr)
        return
    for n in range(start, N + 1):
        arr[idx] = n
        recur(idx + 1, n + 1)


N, M = map(int, input().split())
arr = [0] * M
recur(0, 1)
