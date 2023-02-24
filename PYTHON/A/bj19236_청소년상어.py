from copy import deepcopy


def shark_moves(arr, darr, fishes, cells, dr, dc):
    global answer
    global mx
    for cell in cells:
        r, c = cell[0], cell[1]
        if arr[r][c] == -1:
            continue
        original = deepcopy(arr)  # save originals to restore
        original_d = deepcopy(darr)
        original_f = deepcopy(fishes)

        # eat fish
        fishes[0] = (r, c)
        answer.append(arr[r][c])
        if sum(answer) > mx:
            mx = sum(answer)
        fishes.pop(arr[r][c])
        arr[r][c] = 0  # place shark
        update_arr(arr, darr, fishes, dr, dc)

        # get next cells
        next_cells = []
        shark_d = darr[r][c]
        for i in range(1, 4):
            nr, nc = r + dr[shark_d] * i, c + dc[shark_d] * i
            if not (4 > nr >= 0 and 4 > nc >= 0):  # check index
                continue
            if arr[nr][nc] != -1:  # not empty
                next_cells.append((nr, nc))

        arr[r][c] = -1  # when shark leaves
        shark_moves(arr, darr, fishes, next_cells, dr, dc)

        # restore changes
        arr = original
        darr = original_d
        fishes = original_f
        answer.remove(arr[r][c])
    return


def update_arr(arr, darr, fishes, dr, dc):
    for fish_num in range(1, 17):
        if fishes.get(fish_num) is None:
            continue
        r, c = fishes[fish_num]
        direction = darr[r][c]
        for d in range(8):
            new_d = (direction + d) % 8
            nr, nc = r + dr[new_d], c + dc[new_d]
            if not (4 > nr >= 0 and 4 > nc >= 0):
                continue
            if arr[nr][nc] != 0:  # not a shark
                next_fish_num = arr[nr][nc]
                fishes[next_fish_num] = (r, c)
                fishes[fish_num] = (nr, nc)
                arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]  # swap
                darr[r][c], darr[nr][nc] = darr[nr][nc], new_d
                break


# key -> 0: shark, 1~16: fishes
# value -> (r, c)
fishes = {key: (0, 0) for key in range(-1, 17)}
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
answer = []
mx = 0
arr = [[0] * 4 for _ in range(4)]  # fish numbers on map
darr = [[0] * 4 for _ in range(4)]  # fish directions on map
for r in range(4):
    inp = list(map(int, input().split()))
    for c in range(4):
        fish_number, fish_direction = inp[2 * c], inp[2 * c + 1] - 1
        arr[r][c], darr[r][c] = fish_number, fish_direction
        fishes[fish_number] = (r, c)

shark_moves(arr, darr, fishes, [(0, 0)], dr, dc)
print(mx)
# print(answer)
