from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def possible(gems, mid):
    global N
    cnt = N
    for gem in gems:
        while cnt >= 0:
            cnt -= 1
            gem -= mid
            if gem <= 0:
                break
        if cnt < 0:
            return False
    return True


N, M = map(int, input().split())
gems = [int(input()) for _ in range(M)]

left, right = 0, max(gems)
while left <= right:
    mid = (left + right) // 2
    if possible(gems, mid):
        right = mid - 1
    else:
        left = mid + 1
println(left)
