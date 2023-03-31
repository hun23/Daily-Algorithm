def solve(m, start, comb):
    global N, M, arr
    if m == M:
        print(*comb)
        return
    for n in range(start, N):
        comb[m] = arr[n]
        solve(m + 1, n, comb)
    return

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
solve(0, 0, [0] * M)