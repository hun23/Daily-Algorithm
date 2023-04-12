def get_max(arr):
    return max(sum(arr, []))


def move_blocks(d):
    global arr
    if d == 0:      # up
        for n in range(N):
            fixed = []
            for i in range(N):
                move_this = arr[i][n]
                if move_this == 0:
                    continue
                i -= 1
                while N > i >= 0:
                    # print(arr[i][n])
                    if i in fixed:
                        break
                    if arr[i][n] != 0:
                        if arr[i][n] == move_this:
                            arr[i][n] = move_this * 2
                            arr[i + 1][n] = 0
                            fixed.append(i)
                        else:
                            arr[i + 1][n] = move_this
                    i -= 1
    elif d == 1:    # down
        for n in range(N):
            fixed = []
            for i in range(N-1, -1, -1):  # change
                move_this = arr[i][n]
                if move_this == 0:
                    continue
                i += 1  # change
                while N > i >= 0:
                    # print(arr[i][n])
                    if i in fixed:
                        break
                    if arr[i][n] != 0:
                        if arr[i][n] == move_this:
                            arr[i][n] = move_this * 2
                            arr[i - 1][n] = 0
                            fixed.append(i)
                        else:
                            arr[i - 1][n] = move_this  # change
                    i += 1  # change
    elif d == 2:    # left
        for n in range(N):
            fixed = []
            for i in range(N):
                move_this = arr[n][i]
                if move_this == 0:
                    continue
                i -= 1
                while N > i >= 0:
                    # print(arr[n][i])
                    if i in fixed:
                        break
                    if arr[n][i] != 0:
                        if arr[n][i] == move_this:
                            arr[n][i] = move_this * 2
                            arr[n][i + 1] = 0
                            fixed.append(i)
                        else:
                            arr[n][i + 1] = move_this
                    i -= 1
    else:           # right
        for n in range(N):
            fixed = []
            for i in range(N-1, -1, -1):  # change
                move_this = arr[n][i]
                if move_this == 0:
                    continue
                i += 1  # change
                while N > i >= 0:
                    # print(arr[n][i])
                    if i in fixed:
                        break
                    if arr[n][i] != 0:
                        if arr[n][i] == move_this:
                            arr[n][i] = move_this * 2
                            arr[n][i - 1] = 0
                            fixed.append(i)
                        else:
                            arr[n][i - 1] = move_this  # change
                    i += 1  # change
    return


def solve(cnt):
    global answer, arr
    if cnt == 5:
        return
    # check answer
    temp = get_max(arr)
    if answer < temp:
        answer = temp
    for d in range(4):
        # save & move
        original = [a[:] for a in arr]
        move_blocks(d)
        if cnt == 0:
            print('start_new')
        print(f"move: {'UDLR'[d]}")
        for a in arr:
            print(a)
        # solve
        solve(cnt + 1)
        # reset
        arr = [o[:] for o in original]
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = get_max(arr)
solve(0)
print(answer)
