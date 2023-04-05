from copy import deepcopy


def get_min(arr):
    ret = 2147483647
    for i in range(1, len(arr) - 1):
        ret = min(ret, sum(arr[i]))
    return ret


def rotate(arr, r, c, s):
    while s > 0:
        up_r, up_c = r - s, c - s
        down_r, down_c = r + s, c + s
        # save top & bottom
        top_temp = arr[up_r][up_c: down_c][:]
        down_temp = arr[down_r][up_c + 1: down_c + 1][:]
        # save right & left
        right_temp = []
        for i in range(up_r, down_r):
            right_temp.append(arr[i][down_c])
        left_temp = []
        for i in range(down_r, up_r, -1):
            left_temp.append(arr[i][up_c])
        # move
        arr[up_r][up_c + 1: down_c + 1] = top_temp
        arr[down_r][up_c: down_c] = down_temp
        for idx, i in enumerate(range(up_r + 1, down_r + 1)):
            arr[i][down_c] = right_temp[idx]
        for idx, i in enumerate(range(down_r - 1, up_r - 1, -1)):
            arr[i][up_c] = left_temp[idx]
        s -= 1
    return


def solve(K, path, used):
    global rotations, answer, arr, original
    if K == 0:
        print(path)
        for ro in path:
            rotate(arr, *ro)
            print()
            for a in arr:
                print(a)
        temp = get_min(arr)
        if answer > temp:
            answer = temp
        arr = deepcopy(original)
        return
    for i in range(len(used)):
        if not used[i]:
            used[i] = True
            path.append(rotations[i])
            solve(K - 1, path, used)
            path.pop()
            used[i] = False
    return


N, M, K = map(int, input().split())
arr = [[0] * (M + 2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0] * (M + 2)]
original = deepcopy(arr)
rotations = [list(map(int, input().split())) for _ in range(K)]
answer = 2147483647
solve(K, [], [False] * K)
print(answer)
