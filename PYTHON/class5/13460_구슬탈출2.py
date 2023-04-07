from collections import deque


def move(coordinates, order, d):
    global template
    temp = [t[:] for t in template] # deepcopy original board
    finished = {"R": False, "B": False}
    next_coordinates = {"R": (0, 0), "B": (0, 0)}
    # move till hit wall
    for color in order:
        sr, sc = coordinates[color]
        nr, nc = sr + dr[d], sc + dc[d]
        while temp[nr][nc] in ".":
            nr, nc = nr + dr[d], nc + dc[d]
        # passed all . -> hit R, B, O, #
        if temp[nr][nc] == "O":
            finished[color] = True
        else:  # set color ball at board
            temp[nr - dr[d]][nc - dc[d]] = color
            # save color ball coordinates
            next_coordinates[color] = (nr - dr[d], nc - dc[d])
    return next_coordinates['R'], next_coordinates['B'], finished


def move_and_get_RB(R, B, d):
    # set variables
    rR, cR = R
    rB, cB = B

    order = "RB"
    if rR == rB:  # if in same line
        if d == 2:  # left
            if cR < cB:
                order = "RB"
            else:
                order = "BR"
        elif d == 3:  # right
            if cR < cB:
                order = "BR"
            else:
                order = "RB"
    elif cR == cB:
        if d == 0:  # up
            if rR < rB:
                order = "RB"
            else:
                order = "BR"
        elif d == 1:  # down
            if rR < rB:
                order = "BR"
            else:
                order = "RB"
    return move({"R":R, "B":B}, order, d)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
R, B = [], []
for r in range(N):      # find R B coordinates
    for c in range(M):
        if arr[r][c] == 'R':
            R = (r, c)
            arr[r][c] = '.'
        elif arr[r][c] == 'B':
            B = (r, c)
            arr[r][c] = '.'
template = [a[:] for a in arr]  # deepcopy original board
q = deque([(R, B, 0)])  # up - down - left - right
visited = dict()
visited[(R, B)] = True  # (8 * 8) * (8 * 8 - 1) = ~4000, possible
answer = 11
while q:
    cR, cB, cnt = q.popleft()
    for d in range(4):
        # get next R, B coordinates & check if R or B is out of board
        nR, nB, finished = move_and_get_RB(cR, cB, d)
        if finished["R"] and not finished["B"]:  # if only R is out
            # if answer > cnt + 1:
            #     answer = cnt + 1
            print(cnt + 1)
            exit(0)
        elif finished["B"]:  # if B is out -> stop further searching
            continue
        if visited.get((nR, nB)) is None:
            visited[(nR, nB)] = True
            if cnt + 1 < 10:    # when cnt < 10
                q.append((nR, nB, cnt + 1))
if answer == 11:
    answer = -1
print(answer)
