import sys
from collections import deque
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# r / g / b
# rg / b
# 먼저 순회하며 B 찾기
cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == "B":
            # get b first
            q = deque()
            q.append((r, c))
            arr[r][c] = "X"
            cnt += 1
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if N > nr >= 0 and N > nc >= 0:
                        if arr[nr][nc] == "B":
                            arr[nr][nc] = "X"
                            q.append((nr, nc))
arr_r = deepcopy(arr)
arr_rg = arr
cnt_r = 0
cnt_rg = 0
for r in range(N):
    for c in range(N):
        if arr_r[r][c] == "R":
            # get r
            q = deque()
            q.append((r, c))
            arr_r[r][c] = "X"
            cnt_r += 1
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if N > nr >= 0 and N > nc >= 0:
                        if arr_r[nr][nc] == "R":
                            arr_r[nr][nc] = "X"
                            q.append((nr, nc))
        if arr_r[r][c] == "G":
            # get g
            q = deque()
            q.append((r, c))
            arr_r[r][c] = "X"
            cnt_r += 1
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if N > nr >= 0 and N > nc >= 0:
                        if arr_r[nr][nc] == "G":
                            arr_r[nr][nc] = "X"
                            q.append((nr, nc))
        if arr_rg[r][c] in "RG":
            # get g
            q = deque()
            q.append((r, c))
            arr_rg[r][c] = "X"
            cnt_rg += 1
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if N > nr >= 0 and N > nc >= 0:
                        if arr_rg[nr][nc] in "RG":
                            arr_rg[nr][nc] = "X"
                            q.append((nr, nc))
# print(cnt)
# print(cnt_r)
# print(cnt_rg)
print(f"{cnt + cnt_r} {cnt + cnt_rg}")
# for ar in arr_r:
#     for a in ar:
#         print(a, end="")
#     print()

di = dict()
di[0] = 0
di[2] = 3
recur(n)
def recur(n):
    if ~
    else:
        if di.get(n) != none
            return di[n]
        else:
            