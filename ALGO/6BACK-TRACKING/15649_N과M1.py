from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx):
    global N, M, arr, visited
    if idx == M:
        print(*arr)
        return
    for n in range(1, N + 1):
        if visited[n]:
            continue
        arr[idx] = n
        visited[n] = True
        recur(idx + 1)
        visited[n] = False


N, M = map(int, input().split())
arr = [0] * M
visited = [False] * (N + 1)
recur(0)
