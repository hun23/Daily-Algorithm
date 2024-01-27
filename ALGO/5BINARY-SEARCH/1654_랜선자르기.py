from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def how_many(arr, n):
    ret = 0
    for a in arr:
        ret += a // n
    return ret


K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
arr.sort()

left, right = 1, arr[-1] + 1
while left <= right:
    mid = (left + right) // 2
    if how_many(arr, mid) >= N:
        left = mid + 1
    else:
        right = mid - 1
println(right)
