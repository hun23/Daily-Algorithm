def solve(N, m, start, idx):
    if m == 0:
        for n in range(N):
            if idx & (1<<n):
                print(range(1, N + 1)[n], end="")
                if n != N - 1:
                    print(" ", end="")
        print()
        return
    for n in range(start, N):
        if idx & (1<<n):
            continue
        solve(N, m - 1, n, idx | 1<<n)
    return

N, M = map(int, input().split())
visited = [False] * (1<<N)
solve(N, M, 0, 0)