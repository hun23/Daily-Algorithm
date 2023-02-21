# 시간초과, 한셀씩 봐서 N = 10인 경우 2의 10*10승 경우의수라서 그런듯
def recursion(arr, N, d1, d2, row, col, cnt):
    global mx
    if row == N:
        return cnt
    if col + 1 == N:
        nrow, ncol = row + 1, 0
    else:
        nrow, ncol = row, col + 1

    is_bishop, no_bishop = 0, 0
    d1_idx, d2_idx = col + row, (N - 1) - col + row
    if arr[row][col] == 1 and not d1[d1_idx] and not d2[d2_idx]:
        d1[d1_idx], d2[d2_idx] = True, True
        is_bishop = recursion(arr, N, d1, d2, nrow, ncol, cnt + 1)
        d1[d1_idx], d2[d2_idx] = False, False

    no_bishop = recursion(arr, N, d1, d2, nrow, ncol, cnt)
    mx = max(mx, is_bishop, no_bishop)
    return mx


# idea2 nqueen의 경우 queen은 한 row에 하나씩 밖에 안들어간다.
# bishop의 경우 한 대각선에 하나씩이기 때문에 그런 방식으로
# 한 대각선씩 보면 2의 (2N - 1)승 * N,
# 서로 겹치지 않는 대각선 두개를 따로 보면 2의 N승 * N * 2로 시간이 줄어든다.?
def recursion2(arr, N, dnum, d2, cnt):
    global mx
    if dnum >= 2 * N - 1:
        return cnt
    elif ((2 * N - 1) - dnum) + cnt < mx:  # prunning
        return 0

    # check dnum diagnoal
    for i in range(dnum + 1):
        itercnt += 1
        r, c = i, dnum - i
        if N > r >= 0 and N > c >= 0:
            other_d_idx = (N - 1) - c + r
            if arr[r][c] and not d2[other_d_idx]:
                # put bishop on that diagonal
                d2[other_d_idx] = True
                temp = recursion2(arr, N, dnum + 1, d2, cnt + 1)
                mx = temp if temp > mx else mx
                d2[other_d_idx] = False
    temp = recursion2(arr, N, dnum + 1, d2, cnt)
    mx = temp if temp > mx else mx
    return mx


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d1 = [False] * (2 * N - 1)  # down-left diagonal
d2 = [False] * (2 * N - 1)  # down-right diagonal
a1 = recursion2(arr, N, 0, d2, 0, 1)
a2 = recursion2(arr, N, 1, d2, 0, 1)
print(a1 + a2)
