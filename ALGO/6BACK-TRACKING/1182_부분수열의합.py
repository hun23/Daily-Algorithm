from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, total):
    global N, S, arr, visited, ans
    if idx == N:
        if total == S:
            ans += 1
        return
    
    recur(idx + 1, total)
    recur(idx + 1, total + arr[idx])

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N
ans = 0 if S != 0 else -1
recur(0, 0)
println(ans)
