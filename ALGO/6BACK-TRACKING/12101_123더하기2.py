from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, total):
    global N, K, selected
    if total > N:
        return
    elif total == N:
        K -= 1
        if K == 0:
            print(*selected[:idx], sep="+")
            exit()
        return
    for i in range(1, 4):
        selected[idx] = i
        recur(idx + 1, total + i)


N, K = map(int, input().split())
selected = [0] * N
recur(0, 0)
print(-1)
