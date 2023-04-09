from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    start_points = []
    for n in [0, N - 1]:
        for m in range(M):
            if arr[n][m] == ".":
                start_points.append((n, m))
    for m in [0, M - 1]:
        for n in range(N):
            if arr[n][m] == ".":
                start_points.append((n, m))
    keys = list(input())
    print(start_points)
    print(keys)
    
    # BFS * N?
    