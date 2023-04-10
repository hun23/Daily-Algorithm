from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    keys = list(input())
    keys.extend(list(".$"))
    keys = set(map(lambda x: x.upper(), keys))
    BIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SMALL = "abcdefghijklmnopqrstuvwxyz"
    answer = 0

    # BFS
    visited = [[False] * M for _ in range(N)]
    q, next_q = deque(), deque()
    # first check boundaries
    for r in range(N):
        for c in range(M):
            if r in [0, N-1] or c in [0, M-1]:
                if arr[r][c] == '*':
                    continue
                if arr[r][c] in SMALL:
                    q.append((r, c))
                    keys.add(arr[r][c].upper())
                elif arr[r][c] in BIG:
                    next_q.append((r, c))
                elif arr[r][c] in keys:
                    q.append((r, c))
    # BFS
    while True:
        # q <- next q with key
        i = len(next_q)
        while i > 0:
            r, c = next_q.popleft()
            if arr[r][c] in keys:
                q.append((r, c))
            else:
                next_q.append((r, c))
            i -= 1
        # breakpoint
        if not q:
            break
        # check visited
        for r, c in q:
            if arr[r][c] == '$':
                answer += 1
            visited[r][c] = True
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                char = arr[nr][nc]
                if visited[nr][nc] or arr[nr][nc] == "*":
                    continue
                if arr[nr][nc] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if arr[nr][nc] not in keys:
                        next_q.append((nr, nc))
                        continue
                elif arr[nr][nc] in 'abcdefghijklmnopqrstuvwxyz':
                    keys.add(arr[nr][nc].upper())
                elif arr[nr][nc] == '$':
                    answer += 1
                visited[nr][nc] = True
                q.append((nr, nc))
    print(answer)
