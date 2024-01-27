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


T = int(input())
for t in range(T):
    ans = 0
    N = int(input())
    dots = list(map(int, input().split()))
    dots.sort()
    location = dict()
    for dot in dots:
        location[dot] = True

    for i in range(N):
        left = dots[i]
        for j in range(i + 1, N):
            mid = dots[j]
            if location.get(mid + (mid - left), False):
                ans += 1
    println(ans)
