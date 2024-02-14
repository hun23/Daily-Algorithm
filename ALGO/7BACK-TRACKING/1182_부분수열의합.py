from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, total):
    global N, S
    if idx == N:
        if total == S:
            return 1
        return 0

    ret = 0
    ret += recur(idx + 1, total)
    ret += recur(idx + 1, total + arr[idx])
    return ret


N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N
println(recur(0, 0) + (0 if S != 0 else -1))
