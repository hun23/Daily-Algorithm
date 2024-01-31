from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def possible(num):
    global arr
    cnt = 0
    for i in range(len(arr)):
        if arr[i] >= num:
            cnt += 1
            if cnt == num:
                return True
        else:
            cnt = 0
    return False


N = int(input())
arr = list(map(int, input().split()))
left, right = 1, max(arr) + 1
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        left = mid + 1
    else:
        right = mid - 1
println(right)
