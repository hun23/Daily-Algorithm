from collections import deque

T = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
costs = list(map(lambda x: x**2 + (x - 1) ** 2, range(20 + 2)))
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr = [[0] * N for _ in range(N)]
    # home_lists = []
    # for r in range(N):
    #     inp = input().split()
    #     for c in range(N):
    #         num = int(inp[c])
    #         arr[r][c] = num
    #         if num == 1:
    #             home_lists.append((r, c))

    home_lists = []
    arr = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                home_lists.append((r, c))

    answer = 0
    for k in range(N + 1, -1, -1):
        zido = [[0] * N for _ in range(N)]
        need = costs[k] // M + (1 if costs[k] % M != 0 else 0)

        if len(home_lists) < need:
            continue

        for r, c in home_lists:
            visited = [[-1] * N for _ in range(N)]
            q = deque()
            q.append((r, c))
            visited[r][c] = 0
            zido[r][c] += 1
            while q:
                y, x = q.popleft()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if N > ny >= 0 and N > nx >= 0:
                        if visited[ny][nx] == -1:
                            if visited[y][x] + 1 < k:
                                zido[ny][nx] += 1
                                visited[ny][nx] = visited[y][x] + 1
                                q.append((ny, nx))
        temp = max(sum(zido, []))
        if temp >= need:
            answer = temp
            break
    print(f"#{tc} {answer}")
