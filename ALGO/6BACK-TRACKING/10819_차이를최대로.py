from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx):
    global N, arr, selected, visited, ans
    if idx == N:
        temp = 0
        for i in range(N - 1):
            temp += abs(selected[i] - selected[i + 1])
        if ans < temp:
            ans = temp
        return
    for i in range(N):
        if visited[i]:
            continue
        selected[idx] = arr[i]
        visited[i] = True
        recur(idx + 1)
        visited[i] = False


N = int(input())
arr = list(map(int, input().split()))
selected = [0] * N
visited = [False] * N
ans = 0
recur(0)
println(ans)
