from collections import deque
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())
graph = {key: set() for key in range(1, K + 1)}
garo, sero = dict(), dict()
for k in range(K):  # Bus lines to garo / sero
    b, x1, y1, x2, y2 = map(
        int, sys.stdin.readline().rstrip().split()
    )
    if x1 == x2:  # sero
        y1, y2 = min(y1, y2), max(y1, y2)
        sero.setdefault(x1, []).append((b, y1, y2))
    elif y1 == y2:  # garo
        x1, x2 = min(x1, x2), max(x1, x2)
        garo.setdefault(y1, []).append((b, x1, x2))
sx, sy, ex, ey = map(int, input().split())  # get start & end point

# garo/sero to graph
garo_keys, sero_keys = list(garo.keys()), list(sero.keys())
for n, garo_lines in garo.items():
    # garo compare to sero
    for garo_line in garo_lines:
        st, ed = garo_line[1], garo_line[2]
        for sero_key in sero_keys:
            if st <= sero_key <= ed:
                sero_lines = sero[sero_key]
                for sero_line in sero_lines:
                    if sero_line[1] <= n <= sero_line[2]:
                        graph[garo_line[0]].add(sero_line[0])
                        graph[sero_line[0]].add(garo_line[0])
    # garo compare to garo
    for i in range(len(garo_lines) - 1):
        for j in range(i + 1, len(garo_lines)):
            if not (
                garo_lines[i][2] < garo_lines[j][1]
                or garo_lines[i][1] > garo_lines[j][2]
            ):
                graph[garo_lines[i][0]].add(garo_lines[j][0])
                graph[garo_lines[j][0]].add(garo_lines[i][0])
for m, sero_lines in sero.items():
    # garo compare to garo
    for i in range(len(sero_lines) - 1):
        for j in range(i + 1, len(sero_lines)):
            if not (
                sero_lines[i][2] < sero_lines[j][1]
                or sero_lines[i][1] > sero_lines[j][2]
            ):
                graph[sero_lines[i][0]].add(sero_lines[j][0])
                graph[sero_lines[j][0]].add(sero_lines[i][0])

# BFS
visited = [0] * (K + 1)
q = deque()
# start point - graph / end point - graph
start, end = [], []
try:
    for bnum, st, ed in garo[sy]:
        if st <= sx <= ed:
            start.append(bnum)
except:
    pass
try:
    for bnum, st, ed in sero[sx]:
        if st <= sy <= ed:
            start.append(bnum)
except:
    pass
try:
    for bnum, st, ed in garo[ey]:
        if st <= ex <= ed:
            end.append(bnum)
except:
    pass
try:
    for bnum, st, ed in sero[ex]:
        if st <= ey <= ed:
            end.append(bnum)
except:
    pass
del garo
del sero
for st in start:
    q.append(st)
    visited[st] = 1
for ed in end:
    q.append(ed)
    visited[ed] = -1

answer = 0
while q:
    cur = q.popleft()
    found = False
    # if cur in end:
    #     answer = abs(visited[cur])
    #     break
    for nex in graph[cur]:
        if visited[nex] * visited[cur] < 0:  # 만나면
            found = True
            answer = abs(visited[nex]) + abs(visited[cur])
            break
        if not visited[nex]:
            visited[nex] = visited[cur] + (
                1 if visited[cur] > 0 else -1
            )
            q.append(nex)
    if found:
        break
print(answer)
