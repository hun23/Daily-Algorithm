def solve(m, start, comb):
    global N, M
    if m == M:
        print(*comb)
        return
    for n in range(start, N + 1):
        comb[m] = n
        solve(m + 1, n, comb)
    return

N, M = map(int, input().split())
solve(0, 1, [0] * M)