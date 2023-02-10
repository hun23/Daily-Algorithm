def cut_arr(arr, i):
    len_ = len(arr) // 2
    ret = [[0] * len_ for _ in range(len_)]
    for r in range(len_):
        if i == 0:
            ret[r][:] = arr[r][:len_]
        elif i == 1:
            ret[r][:] = arr[r][len_:]
        elif i == 2:
            ret[r][:] = arr[r + len_][:len_]
        else:
            ret[r][:] = arr[r + len_][len_:]
    return ret


def mysum(arr):
    ret = 0
    for a in arr:
        ret += sum(a)
    return ret


def recursion(arr, cnt):
    if mysum(arr) == 0:
        return (1, 0)
    elif mysum(arr) == len(arr) ** 2:
        return (0, 1)

    white = 0
    blue = 0
    for i in range(4):
        r = recursion(cut_arr(arr, i), cnt - 1)
        white += r[0]
        blue += r[1]
    return (white, blue)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
to_cnt = [2, 4, 8, 16, 32, 64, 128]
cnt = to_cnt.index(N) + 1
white, blue = recursion(arr, cnt)
print(white)
print(blue)
