from collections import deque


def get_max(arr):
    return max(sum(arr, []))


def to_tuple(cnt, arr):
    return (cnt, tuple(sum(arr, [])))

def to_arr(tp):
    global N
    ret = []
    tp = list(*tp)
    for n in range(N + 2):
        s, e = n * (N + 2), (n + 1) * (N + 2)
        ret.append(tp[s:e])
    return ret


def move(arr, reverse, transpose):
    itr = range(1, N + 1)
    move_direction = -1
    if reverse:
        itr = range(N, 0, -1)
        move_direction = 1
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
    ret = [a[:] for a in arr]
    return ret


def move_blocks(arr, d):
    arr = [a[:] for a in arr]
    if d == 0:      # up
        ret = move(arr, False, False)
    elif d == 1:    # down
        ret = move(arr, True, False)
    elif d == 2:    # left
        ret = move(arr, False, True)
    else:           # right
        ret = move(arr, True, True)
    return ret


def solve(cnt):
    global answer, arr, memo, cut_count, call_count
    call_count += 1
    tp = to_tuple(arr, cnt)
    if memo.get(tp) is not None:
        cut_count += 1
        return
    else:
        memo[tp] = True

    temp = get_max(arr)
    if answer < temp:
        answer = temp
    if cnt == 10:
        return
    # check answer
    for d in range(4):
        # save & move
        original = [a[:] for a in arr]
        move_blocks(d)
        # print(f"move: {'UDLR'[d]} / cnt: {cnt}")
        # for a in arr:
        #     print(a)
        # solve
        solve(cnt + 1)
        # reset
        arr = [o[:] for o in original]
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

memo = dict()
N = int(input())
arr = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
answer = 0
cut_count, call_count = 0, 0
# solve(0)
# print(answer)
# print(cut_count)
# print(call_count)

start = to_tuple(0, arr)
start = start
q = deque([start])
memo[start] = True
while q:
    temp = q.popleft()
    cur_cnt, cur = temp[0], to_arr(temp[1:])
    # print("-"*30)
    # print(path)
    # for a in cur:
    #     print(a)
    for d in range(4):
        nex = move_blocks(cur, d)
        value = get_max(nex)
        if answer < value:
            answer = value
        if cur_cnt + 1 >= 10:
            continue
        nex = to_tuple(cur_cnt + 1, nex)
        if memo.get(nex) is None:
            memo[nex] = True
            q.append(nex)
print(answer)
