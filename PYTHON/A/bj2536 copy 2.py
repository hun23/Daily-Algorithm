from collections import deque

M, N = map(int, input().split())
K = int(input())
garo_lines = []
sero_lines = []
graph = {key: [] for key in range(1, K + 1)}
arr = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]
for k in range(K):  # Bus lines to garo / sero
    b, x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    if x1 == x2:  # sero
        sero_lines.append((x1, y1, y2, b))
    elif y1 == y2:  # garo
        garo_lines.append((y1, x1, x2, b))
garo_lines.sort()
sero_lines.sort()
# get start & end point
sx, sy, ex, ey = map(int, input().split())
# garo & garo
for i in range(len(garo_lines) - 1):
    for j in range(i + 1, len(garo_lines)):
        if garo_lines[i][0] == garo_lines[j][0]:
            pass
        # else:
        #     break
# sero & sero
for i in range(len(sero_lines) - 1):
    for j in range(i + 1, len(sero_lines)):
        if sero_lines[i][0] == sero_lines[j][0]:
            pass
        # else:
        #     break
# garo & sero
for i in range(len(garo_lines)):
    for j in range(len(sero_lines)):
        pass
# check start point, end point with graph

# BFS
q = deque()
visited = [False] * (1 + K)
