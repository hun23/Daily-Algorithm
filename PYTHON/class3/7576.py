import sys
from collections import deque

M, N = map(int, input().split())
boxes = []
tomatoes_to_ripe = 0
ripe = 0
q = deque()
for n in range(N):
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    boxes.append(inp)
    for m in range(M):
        if inp[m] == 0:
            tomatoes_to_ripe += 1
        elif inp[m] == 1:
            q.append((n, m))
# print(q)
# BFS
mx_days = 0
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]
while q:
    point = q.popleft()
    day = boxes[point[0]][point[1]]
    if day > mx_days:
        mx_days = day
    for i in range(4):
        nn = point[0] + dn[i]
        nm = point[1] + dm[i]
        if N > nn >= 0 and M > nm >= 0:
            if boxes[nn][nm] == 0:
                boxes[nn][nm] = day + 1
                q.append((nn, nm))
                ripe += 1
    # for b in boxes:
    #     print(b)
if tomatoes_to_ripe - ripe > 0:
    print(-1)
else:
    print(mx_days - 1)
