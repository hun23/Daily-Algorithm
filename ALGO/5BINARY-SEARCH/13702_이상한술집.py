from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def possible(jujeonjas, mid):
    global K
    cnt = K
    for jujeonja in jujeonjas:
        cnt -= jujeonja // mid
        if cnt <= 0:
            return True
    return False


N, K = map(int, input().split())
jujeonjas = [int(input()) for _ in range(N)]

left, right = 1, max(jujeonjas)
while left <= right:
    mid = (left + right) // 2
    if possible(jujeonjas, mid):
        left = mid + 1
    else:
        right = mid - 1
println(right)
