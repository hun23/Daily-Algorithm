from collections import deque


def get_parent(child):
    p = parent[child]
    while p != child:
        child = p
        p = parent[child]
    return p


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# count & mark islands with BFS
island_idx = 1
islands = []
visited = [[False] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] and not visited[r][c]:
            coordinates = []
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                cr, cc = q.popleft()
                arr[cr][cc] = island_idx
                coordinates.append((cr, cc))
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]
                    if not (N > nr >= 0 and M > nc >= 0):
                        continue
                    if arr[nr][nc] != 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            islands.append((island_idx, coordinates))
            island_idx += 1
# for a in arr:
#     print(a)

# get all weights between islands
# adjacency matrix with weight
matrix = [[2147483647] * island_idx for _ in range(island_idx)]
for il in islands:
    idx, coordinates = il
    for r, c in coordinates:
        for d in range(4):
            i = 1
            while True:
                nr, nc = r + dr[d] * i, c + dc[d] * i
                if not (N > nr >= 0 and M > nc >= 0):
                    break
                if arr[nr][nc] == idx:  # when still inside the island
                    break
                if arr[nr][nc] != 0:  # when connected to other island
                    temp = min(matrix[idx][arr[nr][nc]], i - 1)
                    if temp != 1:  # if not impossible
                        matrix[idx][arr[nr][nc]] = temp
                    break
                i += 1
# for a in matrix:
#     print(a)

# Kruskal Algorithm & union-find
answer = 0
parent = [a for a in range(island_idx)]
while True:
    # get min weight and coordinate
    min_ = 2147483647
    min_idx = [0, 0]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
                min_idx = [i, j]
    if min_ == 2147483647:
        break

    # update arr & parent for union find
    mr, mc = min_idx
    matrix[mr][mc], matrix[mc][mr] = 2147483647, 2147483647
    p1, p2 = get_parent(mr), get_parent(mc)
    if p1 != p2:  # different group
        parent[p2] = mr  # connect
        answer += min_  # update answer

for p in range(1, len(parent) - 1):
    if get_parent(p) != get_parent(p + 1):  # if different group exists
        answer = -1

print(answer)
