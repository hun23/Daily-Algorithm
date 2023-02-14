from copy import deepcopy


def update(visited):
    visited = deepcopy(original)
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 2:
                # right daegak
                for i in range(1, N):
                    try:
                        visited[r + i][c + i] = 1
                    except:
                        pass
                    try:
                        visited[r + i][c - i] = 1
                    except:
                        pass
                    try:
                        visited[r - i][c + i] = 1
                    except:
                        pass
                    try:
                        visited[r - i][c - i] = 1
                    except:
                        pass


def recursion(arr, visited, sr, sc, depth):
    for r in range(sr, N):
        for c in range(sc, N):
            if visited[r][c] == 0 and arr[r][c] == 1:
                for b in range(2):
                    if b:
                        visited[r][c] = 2
                        update(visited)
                        depth = recursion(
                            arr, visited, sr, sc, depth + 1
                        )
                        visited[r][c] = 0
                        update(visited)
                    else:
                        visited[r][c] = 1
    return depth


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 3차원 visited -> 2차원 arr * (0, 1: 비숍여부)
# visited = [[[0] * N for _ in range(N)] for _ in range(2)]
visited = [[0] * N for _ in range(N)]
original = deepcopy(visited)

# bfs, dfs -> 불가능, 서로 떨어져 있을 수 있다.
# 따라서, (r, c)돌아야할듯? - > 재귀
answer = recursion(arr, visited, 0, 0, 0)
print(answer)


# start_point는 아무거나 잡아도 ok
# 경우의수는 해당 point에 비숍이 있거나 없거나 두가지뿐이기 때문
# get start point
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 1:
#             sr, sc = r, c
#             break
# delta & BFS
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# mx = 0
# for i in range(2):  # 0: 처음비숍없음, 1: 처음비숍있음
#     q = deque()
#     q.append((sr, sc, i))
#     visited[i][sr][sc] = i
#     while q:
#         r, c, b = q.popleft()
#         cnt = visited[b][r][c]
#         if cnt > mx:
#             mx = cnt
#         for nb in range(2):  # is_bishop?
#             for d in range(4):  # directions
#                 nr, nc = r + dr[d], c + dc[d]
#                 if N > nr >= 0 and N > nc >= 0:
#                     if visited[nb][nr][nc] == -1:
#                         visited[nb][nr][nc] = cnt + 1
#                         q.append((nr, nc, nb))
# print(mx)

# # delta & DFS
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# mx = 0
# for i in range(2):  # 0: 처음비숍없음, 1: 처음비숍있음
#     stack = []
#     stack.append((sr, sc, i))
#     b_cnt = i
#     while stack:
#         r, c, b = stack.pop()
#         if b:
#             b_cnt -= 1
#         if visited[b][r][c] == 0:
#             visited[b][r][c] = visited[]
#             for nb in range(2):  # is_bishop?
#                 for d in range(4):  # direction
#                     nr, nc = r + dr[d], c + dc[d]
#                     if N > nr >= 0 and N > nc >= 0:
#                         stack.append((nr, nc, nb))
#                         if nb:
#                             b_cnt += 1
#                             if b_cnt > mx:
#                                 mx = b_cnt
# print(mx)
