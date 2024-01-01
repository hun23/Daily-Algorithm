N, M, K = map(int, input().split())
ans = (N + M - K) // 3

for a in range(ans, -1, -1):
    if N >= a * 2 and M >= a:
        print(a)
        exit()