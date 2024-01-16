from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, K = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
ans = -100 * 100000
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
for i in range(K, N + 1):
    temp = prefix_sum[i] - prefix_sum[i - K]
    if ans < temp:
        ans = temp
println(ans)
