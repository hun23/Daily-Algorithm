from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def get_prefix_sum(N, arr):
    prefix_sum = [0] * N
    prefix_sum[0] = arr[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum


# def get_dictionary(prefix_sum):
#     di = dict()
#     n = len(prefix_sum)
#     for i in range(n):
#         for j in range(i, n):
#             if i == 0:
#                 diff = prefix_sum[j]
#             else:
#                 diff = prefix_sum[j] - prefix_sum[i - 1]
#             di[diff] = di.get(diff, 0) + 1
#     return di


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

prefix_sum_A = get_prefix_sum(N, A)
prefix_sum_B = get_prefix_sum(N, B)

ans = 0
for i in range(N):
    for j in range(i, N):
        temp_A, temp_B = prefix_sum_A[j], prefix_sum_B[j]
        if i != 0:
            temp_A -= prefix_sum_A[i - 1]
            temp_B -= prefix_sum_B[i - 1]
        if temp_A == temp_B:
            ans += 1
println(ans)
