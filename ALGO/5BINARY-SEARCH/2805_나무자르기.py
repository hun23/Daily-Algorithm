from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def how_many(arr, n):
    ret = 0
    for a in arr:
        temp = a - n
        if temp > 0:
            ret += temp
    return ret


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

left, right = 1, arr[-1]
while left <= right:
    mid = (left + right) // 2
    if how_many(arr, mid) >= M:
        left = mid + 1
    else:
        right = mid - 1
println(right)
