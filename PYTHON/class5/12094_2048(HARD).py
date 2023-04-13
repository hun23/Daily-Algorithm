def get_max(arr):
    return max(sum(arr, []))


def to_tuple(cnt, arr):
    return (cnt, tuple(sum(arr, [])))


def move(reverse, transpose):
    itr = range(1, N + 1)
    move_direction = -1
    if reverse:
        itr = range(N, 0, -1)
        move_direction = 1
    global arr
    for n in range(1, N + 1):
        fixed = []
        for i in itr:
            move_this = arr[i][n]
            if transpose:
                move_this = arr[n][i]
            if move_this == 0:
                continue
            next_idx = i + (1 * move_direction)
            while N + 1 >= next_idx >= 0:
                next_cell = arr[n][next_idx] if transpose else arr[next_idx][n]
                if next_cell == 0:
                    next_idx += (1 * move_direction)
                    continue

                if next_cell == -1:             # hit wall
                    if transpose:
                        arr[n][i] = 0  # set original cell to zero
                        arr[n][next_idx + (-1 * move_direction)] = move_this
                    else:
                        arr[i][n] = 0  # set original cell to zero
                        arr[next_idx + (-1 * move_direction)][n] = move_this
                elif next_cell == move_this and next_idx not in fixed:    # can sum
                    if transpose:
                        arr[n][i] = 0
                        arr[n][next_idx] = move_this * 2
                    else:
                        arr[i][n] = 0
                        arr[next_idx][n] = move_this * 2
                    fixed.append(next_idx)
                else:                           # other number
                    if transpose:
                        arr[n][i] = 0
                        arr[n][next_idx + (-1 * move_direction)] = move_this
                    else:
                        arr[i][n] = 0
                        arr[next_idx + (-1 * move_direction)][n] = move_this
                break


def move_blocks(d):
    global arr
    if d == 0:      # up
        move(False, False)
    elif d == 1:    # down
        move(True, False)
    elif d == 2:    # left
        move(False, True)
    else:           # right
        move(True, True)
    return


def solve(cnt):
    global arr, dp, call_count

    call_count += 1

    tupled = to_tuple(cnt, arr)
    if dp.get(tupled) is not None:
        return dp[tupled]

    if cnt == 10:
        return get_max(arr)

    # dp
    ret = 0
    # check answer
    for d in range(4):
        # save & move
        original = [a[:] for a in arr]
        move_blocks(d)
        # print(f"move: {'UDLR'[d]} / cnt: {cnt}")
        # for a in arr:
        #     print(a)
        # solve
        ret = max(ret, solve(cnt + 1))
        # reset
        arr = [o[:] for o in original]
    dp[tupled] = ret
    return dp[tupled]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dp = dict()

N = int(input())
arr = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
call_count = 0
print(solve(0))
# print(call_count)