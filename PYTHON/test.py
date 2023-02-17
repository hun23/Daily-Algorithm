import random
from tqdm import tqdm
import time

# 시간초과, 한셀씩 봐서 N = 10인 경우 2의 10*10승 경우의수라서 그런듯
def recursion(arr, N, d1, d2, row, col, cnt):
    global fcnt1
    global mx
    fcnt1 += 1
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
def recursion2(arr, N, dnum, d2, cnt, prunning):
    global fcnt2
    global mx
    global itercnt
    fcnt2 += 1
    # global bit
    if dnum >= 2 * N - 1:
        # if cnt >= 7:
        #     print(f"cnt:{cnt}")
        #     for b in bit:
        #         print(*b, sep=" ")
        #     print()
        return cnt
    elif ((2 * N - 1) - dnum) + cnt < mx:
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
                # temp = bit[r][c]
                # bit[r][c] = "Y"
                temp = recursion2(
                    arr, N, dnum + 1 + prunning, d2, cnt + 1, prunning
                )
                mx = temp if temp > mx else mx
                d2[other_d_idx] = False
                # bit[r][c] = temp
    # mx = max(mx, recursion2(arr, N, dnum + 1, d2, cnt))
    temp = recursion2(arr, N, dnum + 1 + prunning, d2, cnt, prunning)
    mx = temp if temp > mx else mx
    return mx


niter = range(8, 10)
cals = []
fcnt1sum, fcnt2sum = 0, 0
itercntsum1, itercntsum2 = 0, 0
for nit in niter:
    T = 100
    # T = 10 ** (10 - nit)
    # if nit <= 6:
    #     T //= 100
    # elif nit <= 8:
    #     T //= 10
    t1, t2 = 0, 0
    itercnt, itercnt1, itercnt2 = 0, 0, 0
    not_goot = []
    not_good_as = []
    fcnt1, fcnt2 = 0, 0
    for i in tqdm(range(T)):
        # N = int(input())
        # N = random.randint(3, 6)
        N = nit
        # bit = [["X"] * N for _ in range(N)]
        # arr = [list(map(int, input().split())) for _ in range(N)]
        arr = [[1] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                rr = random.randint(1, 100)
                if rr > 70:
                    arr[r][c] = 0
        # print(arr)
        # for r in range(N):
        #     for c in range(N):
        #         if arr[r][c] == 1:
        #             bit[r][c] = "."
        d1 = [False] * (2 * N - 1)  # down-left diagonal
        d2 = [False] * (2 * N - 1)  # down-right diagonal
        d22 = [False] * (2 * N - 1)  # down-right diagonal

        st1 = time.time()
        mx = 0
        a11 = recursion2(arr, N, 0, d22, 0, 1)
        mx = 0
        a12 = recursion2(arr, N, 1, d22, 0, 1)
        a1 = a11 + a12
        # a1 = recursion2(arr, N, 0, d22, 0, False)
        ed1 = time.time()
        # print(f"N:{N} a1time:{ed1 - st1}")
        fcnt1 = fcnt2
        itercnt1 = itercnt
        itercntsum1 += itercnt1
        fcnt1sum += fcnt1
        fcnt2 = 0
        itercnt = 0

        st2 = time.time()
        mx = 0
        a2 = recursion2(arr, N, 0, d22, 0, 0)
        ed2 = time.time()
        # print(f"N:{N} a2time:{ed2 - st2}")
        fcnt2sum += fcnt2
        itercnt2 = itercnt
        itercntsum2 += itercnt2

        t1 += ed1 - st1
        t2 += ed2 - st2
        if a1 != a2:
            not_goot.append(arr)
            not_good_as.append((N, a1, a2))

    cals.append((nit, t1, t2, fcnt1, fcnt2, itercnt1, itercnt2))
    for i in range(len(not_goot)):
        N, a1, a2 = (
            not_good_as[i][0],
            not_good_as[i][1],
            not_good_as[i][2],
        )
        print(f"N:{N} a1:{a1}, a2:{a2}")
        print(not_goot[i])
    # print(f"t1:{t1} / t2:{t2}")
    # print(f"f1:{fcnt1} / f2:{fcnt2}")
    # print(f"diff:{fcnt1 - fcnt2}")
    # try:
    #     print(f"ratio: {t2/t1}")
    # except:
    #     pass
for cc in cals:
    nit, t1, t2, fcnt1, fcnt2, i1, i2 = cc
    print(
        f"{nit}--------------------------------------------------------"
    )
    print(f"i: b:{i2}/g:{i1} / ratio:{i2/i1}")
    # print(cc[1:])
    # try:
    #     print(f"ratio:{t2/t1} / fcntRatio:{fcnt2/fcnt1}")
    # except:
    #     print(
    #         f"ratio:{(t2 + 1)/(t1 + 1)} / fcntRatio:{(fcnt2sum + 1)/(fcnt1sum + 1)}"
    #     )
    # print(f"iterRatio:{i1/i2}")
