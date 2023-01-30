import sys
from collections import deque

# recursion error
def dfs(arr, visited, start):
    r = start[0]
    c = start[1]
    if not visited[r][c]:
        visited[r][c] = True
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if n > nr >= 0 and m > nc >= 0:
                if arr[nr][nc] == 1:
                    dfs(arr, visited, (nr, nc))
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        arr[y][x] = 1
    answer = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 1 and not visited[row][col]:
                # dfs(arr, visited, (row, col)) => recursion error
                # bfs
                q = deque()
                q.append((row, col))
                while q:
                    r, c = q.pop()
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if n > nr >= 0 and m > nc >= 0:
                            if (
                                arr[nr][nc] == 1
                                and not visited[nr][nc]
                            ):
                                visited[nr][nc] = True
                                q.append((nr, nc))
                answer += 1
    print(answer)
