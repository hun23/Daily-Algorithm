from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

H, W = map(int, input().split())
heights = list(map(int, input().split()))

prefix_max = [0] * W
prefix_max[0] = heights[0]
suffix_max = [0] * W
suffix_max[-1] = heights[-1]
for i in range(1, W):
    h = heights[i]
    prefix_max[i] = h if h > prefix_max[i - 1] else prefix_max[i - 1]
for i in range(W - 2, -1, -1):
    h = heights[i]
    suffix_max[i] = h if h > suffix_max[i + 1] else suffix_max[i + 1]
ans = 0
for i in range(W):
    ans += (min(prefix_max[i], suffix_max[i]) - heights[i])
println(ans)
