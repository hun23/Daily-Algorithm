from collections import deque
# recursion error
# def solve(idx, distance, crashed):
#     global N, M, answer, arr, visited
#     r, c = divmod(idx, M)
#     if idx == N * M - 1:
#         if answer > distance:
#             answer = distance
#         return
#     if visited[r][c]:
#         return
#     visited[r][c] = True
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if not (0 <= nr < N and 0 <= nc < M):
#             continue
#         if arr[nr][nc] == 1:
#             if not crashed:
#                 solve(nr * M + nc, distance + 1, True)
#             continue
#         solve(nr * M + nc, distance + 1, crashed)
#     visited[r][c] = False
#     return


def solve2(arr, N, M):
    visited = [[[1000000] * M for _ in range(N)] for _ in range(2)]
    q = deque()
    q.append((0, 0, 0))  # r, c, crashed
    visited[0][0][0] = 1
    visited[1][0][0] = 1
    while q:
        r, c, crashed = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[crashed][nr][nc] != 1000000:
                continue
            if arr[nr][nc] == 1:
                if not crashed:
                    visited[crashed][nr][nc] = visited[crashed][r][c] + 1
                    visited[1][nr][nc] = visited[0][nr][nc]
                    q.append((nr, nc, 1))
                continue
            visited[crashed][nr][nc] = visited[crashed][r][c] + 1
            q.append((nr, nc, crashed))
    answer = min(visited[0][N - 1][M - 1], visited[1][N - 1][M - 1])
    # for v in visited[0]:
    #     print(v)
    # print('\n')
    # for v in visited[1]:
    #     print(v)
    if answer != 1000000:
        return answer
    return -1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
# solve(0, 1, False)  # include start_point in answer -> start distance == 1
print(solve2(arr, N, M))
