from collections import deque
from copy import deepcopy

def move(coordinates, order, d):
    global template
    temp = deepcopy(template)
    finished = {"R": False, "B": False}
    # move till hit wall
    for color in order:
        sr, sc = coordinates[color]
        nr, nc = sr + dr[d], sc + dc[d]
        while temp[nr][nc] in ".O":
            nr, nc = nr + dr[d], nc + dc[d]
        if temp[nr][nc] == "O":
            finished[color] = True
        else:
            temp[nr][nc] = color
    return R, B, finished


def move_and_get_RB(R, B, d):
    # set variables
    rR, cR = R
    rB, cB = B

    order = "RB"
    if rR == rB:  # if in same line
        if d == 2:
            if cR < cB:
                order = "RB"
            else:
                order = "BR"
        elif d == 3:
            if cR < cB:
                order = "BR"
            else:
                order = "RB"
    elif cR == cB:
        if d == 0:
            if rR < rB:
                order = "BR"
            else:
                order = "RB"
        elif d == 1:
            if rR < rB:
                order = "RB"
            else:
                order = "BR"
    return move({"R":R, "B":B}, order, d)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
R, B = [], []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'R':
            R = (r, c)
            arr[r][c] = '.'
        elif arr[r][c] == 'B':
            B = (r, c)
            arr[r][c] = '.'
template = deepcopy(arr)
q = deque([(R, B, 0)])  # up - down - left - right
visited = dict()
visited[(R, B)] = True  # (8 * 8) * (8 * 8 - 1) = ~4000, possible
while q:
    cR, cB, cnt = q.popleft()
    for d in range(4):
        nR, nB, finished = move_and_get_RB(cR, cB, d)
        if finished["R"] and not finished["B"]:
            print(cnt + 1)
            exit(0)
        elif finished["B"]:
            continue
        if visited.get((nR, nB)) is None:
            visited[(nR, nB)] = True
            q.append((nR, nB, cnt + 1))
print(-1)
