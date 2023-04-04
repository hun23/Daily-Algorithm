def solve(N, used, idx, before):
    global dp, path
    if idx == N:
        # print(path)
        return adjM[before][path[0]]

    if dp[idx][used]:
        return dp[idx][used]
    
    min_val = BIG
    for n in range(N):
        if used & (1 << n):
            continue
        path.append(n)
        if before == -1:
            min_val = min(min_val, solve(N, used | (1 << n), idx + 1, n))
        else:
            min_val = min(min_val, solve(N, used | (1 << n), idx + 1, n) + adjM[before][n])
        path.pop()
    dp[idx][used] = min_val
    print()
    for d in dp:
        print(d)
    return dp[idx][used]


N = int(input())
adjM = [list(map(int, input().split())) for _ in range(N)]
BIG = 16 * 1000001
dp = [[0] * (1 << N) for _ in range(N)]
path = []
answer = solve(N, 0, 0, -1)
print(answer)