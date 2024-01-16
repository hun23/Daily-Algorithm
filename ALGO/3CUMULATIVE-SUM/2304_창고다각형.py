from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N = int(input())
arr = [0] * 1001
left_max, right_max = 1001, 0
for n in range(N):
    L, H = map(int, input().split())
    arr[L] = H
right_max = 0

prefix_max = [0] * 1001
prefix_max[0] = arr[0]
suffix_max = [0] * 1001
suffix_max[-1] = arr[-1]
for i in range(1, 1001):
    h = arr[i]
    prefix_max[i] = h if h > prefix_max[i - 1] else prefix_max[i - 1]
for i in range(1001 - 2, -1, -1):
    h = arr[i]
    suffix_max[i] = h if h > suffix_max[i + 1] else suffix_max[i + 1]
# println(prefix_max)
# println(suffix_max)

ans = 0
for i in range(1001):
    diff = min(prefix_max[i], suffix_max[i])
    ans += diff
println(ans)
