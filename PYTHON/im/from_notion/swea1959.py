T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    if N > M:
        big = list(map(int, input().split()))
        small = list(map(int, input().split()))
    else:
        N, M = M, N
        small = list(map(int, input().split()))
        big = list(map(int, input().split()))
    mx = 0
    for i in range(N - M + 1):
        temp = 0
        for m in range(M):
            temp += big[i + m] * small[m]
        if temp > mx:
            mx = temp
    print(f"#{tc} {mx}")
