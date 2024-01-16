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


def get_dictionary(prefix_sum):
    di = dict()
    n = len(prefix_sum)
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                diff = prefix_sum[j]
            else:
                diff = prefix_sum[j] - prefix_sum[i - 1]
            di[diff] = di.get(diff, 0) + 1
    return di


T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

prefix_sum_A = get_prefix_sum(N, A)
prefix_sum_B = get_prefix_sum(M, B)

di_A = get_dictionary(prefix_sum_A)
di_B = get_dictionary(prefix_sum_B)

ans = 0
sorted_di_B_keys = sorted(list(di_B.keys()))
for a_key, a_val in di_A.items():
    diff = T - a_key
    left, right = 0, len(sorted_di_B_keys) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_di_B_keys[mid] > diff:
            right = mid - 1
        elif sorted_di_B_keys[mid] < diff:
            left = mid + 1
        else:
            break
    if diff == sorted_di_B_keys[mid]:
        # println(f"diff:{diff}, mid:{mid}, key:{sorted_di_B_keys[mid]}")
        ans += a_val * di_B[sorted_di_B_keys[mid]]
println(ans)
