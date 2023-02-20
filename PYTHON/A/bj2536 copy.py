from collections import deque

M, N = map(int, input().split())
K = int(input())
bus_lines = dict()
arr = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]
for k in range(K):  # Bus lines to garo / sero
    b, x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    bus_lines[b] = (x1, y1, x2, y2)
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            arr[y][x][b] = 1
# get start & end point
sx, sy, ex, ey = map(int, input().split())
print(arr)
q = deque()
visited = [False] * (1 + K)
for i in range(K + 1):
    if arr[sy][sx][i] == 1:
        q.append((i, [i]))

endlines = []
for j in range(K + 1):
    if arr[ey][ex][j] == 1:
        endlines.append(j)

while q:
    bus_num, history = q.popleft()
    if bus_num in endlines:
        print("break")
        print(history)
        print(len(history))
        break
    x1, y1, x2, y2 = bus_lines[bus_num]
    next_nums = set()
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            possible_lines = arr[y][x]
            for j in range(len(possible_lines)):
                if possible_lines[j] == 1:
                    next_nums.add(j)
    for nex in next_nums:
        if not visited[nex]:
            visited[nex] = True
            temp = history[:]
            temp.append(nex)
            q.append((nex, temp))

# print(garo)
# print(sero)
# # garo/sero to graph
# garo_keys, sero_keys = list(garo.keys()), list(sero.keys())
# for n, garo_lines in garo.items():
#     # garo compare to sero
#     for garo_line in garo_lines:
#         st, ed = garo_line[1], garo_line[2]
#         for sero_key in sero_keys:
#             if st <= sero_key <= ed:
#                 sero_lines = sero[sero_key]
#                 for sero_line in sero_lines:
#                     if sero_line[1] <= n <= sero_line[2]:
#                         graph[garo_line[0]].add(sero_line[0])
#                         graph[sero_line[0]].add(garo_line[0])
#     # garo compare to garo
#     for i in range(len(garo_lines) - 1):
#         for j in range(i + 1, len(garo_lines)):
#             if not (
#                 garo_lines[i][2] < garo_lines[j][1]
#                 and garo_lines[i][1] > garo_lines[j][2]
#             ):
#                 graph[garo_lines[i][0]].add(garo_lines[j][0])
#                 graph[garo_lines[j][0]].add(garo_lines[i][0])
# for m, sero_lines in sero.items():
#     # garo compare to garo
#     for i in range(len(sero_lines) - 1):
#         for j in range(i + 1, len(sero_lines)):
#             if not (
#                 sero_lines[i][2] < sero_lines[j][1]
#                 and sero_lines[i][1] > sero_lines[j][2]
#             ):
#                 graph[sero_lines[i][0]].add(sero_lines[j][0])
#                 graph[sero_lines[j][0]].add(sero_lines[i][0])
# print(graph)

# # BFS
# visited = [False] * (K + 1)
# q = deque()
# # start point - graph / end point - graph
# try:
#     start_garos = list(map(lambda x: x[0], garo[sy]))
# except:
#     start_garos = []
# try:
#     start_seros = list(map(lambda x: x[0], sero[sx]))
# except:
#     start_seros = []
# try:
#     end_garos = list(map(lambda x: x[0], garo[ey]))
# except:
#     end_garos = []
# try:
#     end_seros = list(map(lambda x: x[0], sero[ex]))
# except:
#     end_seros = []
# starts = start_garos + start_seros
# ends = end_garos + end_seros
# for st in starts:
#     q.append((st, [st]))
#     visited[st] = True
# print(q)
# answer = 0
# while q:
#     cur, cnt = q.popleft()
#     print(f"cur:{cur} / {cnt}")
#     if cur in ends:
#         answer = cnt
#     for nex in graph[cur]:
#         if not visited[nex]:
#             visited[nex] = True
#             temp = cnt[:]
#             temp.append(nex)
#             q.append((nex, temp))
# print(answer)
