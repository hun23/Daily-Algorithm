def solve(m, comb, used):
    global N, M, arr
    if m == M:
        print(*comb)
        return
    for n in range(N):
        if used & (1<<n):
            continue
        comb[m] = arr[n]
        solve(m + 1, comb, used | (1<<n))
    return

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
solve(0, [0] * M, 0)