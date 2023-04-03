N = int(input())
M = int(input())
adjM = [[0] * N for _ in range(N)]
for m in range(M):
    a, b, c = map(int, input().split())
    cost = adjM[a - 1][b - 1]
    if cost:
        adjM[a - 1][b - 1] = min(c, cost)
    else:
        adjM[a - 1][b - 1] = c

# Floyd-Warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ik, kj = adjM[i][k], adjM[k][j]
            if ik and kj:
                print(ik, kj)
                if adjM[i][j]:
                    adjM[i][j] = min(adjM[i][j], ik + kj)
                else:
                    adjM[i][j] =ik + kj
for a in adjM:
    print(*a)
