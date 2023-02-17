# def recursion(arr, N, checks, row, col, cnt):
#     global bit
#     if row == N:
#         if cnt >= 6:
#             print(f"cnt:{cnt}")
#             for b in bit:
#                 print(*b, sep=" ")
#             print()
#         return cnt
#     is_bishop, no_bishop = 0, 0
#     d1, d2 = checks[0], checks[1]
#     for i in range(col, N):  # check columns
#         if arr[row][i] == 0:  # if cell is not available
#             continue
#         d1_idx, d2_idx = i + row, (N - 1) - i + row
#         # check other bishops in d1, d2
#         if not d1[d1_idx] and not d2[d2_idx]:
#             d1[d1_idx], d2[d2_idx] = True, True
#             bit[row][i] = i
#             if i + 1 == N:
#                 is_bishop = recursion(
#                     arr, N, checks, row + 1, 0, cnt + 1
#                 )
#             else:
#                 is_bishop = recursion(
#                     arr, N, checks, row, i + 1, cnt + 1
#                 )
#             d1[d1_idx], d2[d2_idx] = False, False
#             if arr[row][i] == 1:
#                 bit[row][i] = "O"
#             else:
#                 bit[row][i] = "X"
#             if i + 1 == N:
#                 no_bishop = recursion(arr, N, checks, row + 1, 0, cnt)
#             else:
#                 no_bishop = recursion(arr, N, checks, row, i + 1, cnt)

#     return max(is_bishop, no_bishop)


def recursion(arr, N, checks, row, col, cnt):
    # global bit
    if row == N:
        # if cnt >= 7:
        # print(f"cnt:{cnt}")
        # for b in bit:
        #     print(*b, sep=" ")
        # print()
        return cnt
    if col + 1 == N:
        nrow, ncol = row + 1, 0
    else:
        nrow, ncol = row, col + 1

    is_bishop, no_bishop = 0, 0
    d1, d2 = checks[0], checks[1]
    d1_idx, d2_idx = col + row, (N - 1) - col + row
    if arr[row][col] == 1 and not d1[d1_idx] and not d2[d2_idx]:
        d1[d1_idx], d2[d2_idx] = True, True
        # temp = bit[row][col]
        # bit[row][col] = "Y"
        is_bishop = recursion(arr, N, checks, nrow, ncol, cnt + 1)
        d1[d1_idx], d2[d2_idx] = False, False
        # bit[row][col] = temp

    no_bishop = recursion(arr, N, checks, nrow, ncol, cnt)
    return max(is_bishop, no_bishop)

    # is_bishop, no_bishop = 0, 0
    # d1, d2 = checks[0], checks[1]
    # for i in range(col, N):  # check columns
    #     if arr[row][i] == 0:  # if cell is not available
    #         continue
    #     d1_idx, d2_idx = i + row, (N - 1) - i + row
    #     # check other bishops in d1, d2
    #     if not d1[d1_idx] and not d2[d2_idx]:
    #         d1[d1_idx], d2[d2_idx] = True, True
    #         bit[row][i] = i
    #         if i + 1 == N:
    #             is_bishop = recursion(
    #                 arr, N, checks, row + 1, 0, cnt + 1
    #             )
    #         else:
    #             is_bishop = recursion(
    #                 arr, N, checks, row, i + 1, cnt + 1
    #             )
    #         d1[d1_idx], d2[d2_idx] = False, False
    #         if arr[row][i] == 1:
    #             bit[row][i] = "O"
    #         else:
    #             bit[row][i] = "X"
    #         if i + 1 == N:
    #             no_bishop = recursion(arr, N, checks, row + 1, 0, cnt)
    #         else:
    #             no_bishop = recursion(arr, N, checks, row, i + 1, cnt)

    # return max(is_bishop, no_bishop)


N = int(input())
# bit = [["X"] * N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 1:
#             bit[r][c] = "."
d1 = [False] * (2 * N - 1)  # down-left diagonal
d2 = [False] * (2 * N - 1)  # down-right diagonal
checks = [d1, d2]

answer = recursion(arr, N, checks, row=0, col=0, cnt=0)
print(answer)
