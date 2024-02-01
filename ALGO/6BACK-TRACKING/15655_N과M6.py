from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, start):
    global N, M, arr, ans
    if idx == M:
        print(*ans)
        return
    for n in range(start, N):
        ans[idx] = arr[n]
        recur(idx + 1, n + 1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * M
recur(0, 0)
