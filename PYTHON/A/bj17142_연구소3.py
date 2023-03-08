from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(arr, to_fill):
    global answer
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    temp_mx = 0
    for c in case:
        q.append(c)
        visited[c[0]][c[1]] = 0
    while q:
        r, c = q.popleft()
        if answer <= visited[r][c]:
            return

        if temp_mx < visited[r][c]:
            temp_mx = visited[r][c]
        to_fill.remove((r, c))

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc] == -1 and arr[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

    if temp_mx < answer:
        answer = temp_mx

    temp_mx = -1
    for r in range(N):
        for c in range(N):
            if visited[r][c] > temp_mx:
                temp_mx = visited[r][c]
            # not visited & not wall
            if visited[r][c] == -1 and arr[r][c] != 1:
                return
    if temp_mx != -1 and answer > temp_mx:
        answer = temp_mx
    return



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == 2]
empties = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == 0]
answer = float("inf")

# delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# get combinations
combs = combinations(starts, M)
for case in combs:  # check each case
    bfs(arr, deepcopy(empties))
print(answer)
