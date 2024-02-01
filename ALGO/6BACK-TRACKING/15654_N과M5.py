from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx):
    global N, M, arr, ans, visited
    if idx == M:
        print(*ans)
        return
    for n in range(N):
        if visited[n]:
            continue
        visited[n] = True
        ans[idx] = arr[n]
        recur(idx + 1)
        visited[n] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * N
ans = [0] * M
recur(0)
