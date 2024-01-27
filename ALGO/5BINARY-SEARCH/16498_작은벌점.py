from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def score(a, b, c):
    return abs(max(a, b, c) - min(a, b, c))


A, B, C = map(int, input().split())
A_list = sorted(list(map(int, input().split())))
B_list = sorted(list(map(int, input().split())))
C_list = sorted(list(map(int, input().split())))

ans = 2 * 100_000_000 + 1
for a in A_list:
    for b in B_list:
        big, small = (a, b) if a > b else (b, a)
        if big - small >= ans:
            continue

        left, right = 0, C - 1
        while left <= right:
            mid = (left + right) // 2
            if big >= C_list[mid] >= small:
                ans = min(ans, big - small)
                break
            if C_list[mid] < small:
                left = mid + 1
            elif C_list[mid] > big:
                right = mid - 1
        if C > left >= 0:
            ans = min(ans, score(big, small, C_list[left]))
        if 0 <= right < C:
            ans = min(ans, score(big, small, C_list[right]))
println(ans)
