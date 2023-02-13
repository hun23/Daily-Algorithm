import sys


def is_pal(arr, trns, r, c, mx_pal_len):
    # check horizontally
    ret = mx_pal_len
    for pal_len in range(
        mx_pal_len + 1, 100 - c + 1
    ):  # mxpallen ~ 100-c+1
        if arr[r][c : c + pal_len] == arr[r][c : c + pal_len][::-1]:
            ret = pal_len
    # check vertically
    for pal_len in range(ret + 1, 100 - r + 1):  # ret ~ 100-r+1
        if trns[c][r : r + pal_len] == trns[c][r : r + pal_len][::-1]:
            ret = pal_len
    return ret


with open("./input.txt", "rb") as fr:
    for tc in range(1, 11):
        # tc = int(input())
        # arr = [list(input()) for _ in range(100)]
        tc = int(fr.readline().rstrip())
        arr = [list(fr.readline().rstrip()) for _ in range(100)]
        trns = list(zip(*arr))  # transpose
        mx_pal_len = 1
        for r in range(100):
            for c in range(100):
                mx_pal_len = is_pal(arr, trns, r, c, mx_pal_len)
        print(f"#{tc} {mx_pal_len}")
