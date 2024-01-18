from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

ans = 0
left, right = 0, 1
while left <= right and right < N + 1:
    temp_sum = prefix_sum[right] - prefix_sum[left]
    if temp_sum == M:
        ans += 1
        left += 1
        right += 1
    elif temp_sum > M:
        left += 1
    elif temp_sum < M:
        right += 1
println(ans)
