from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N = int(input())
arr = list(map(int, input().split()))
max_diff = 2_000_000_000
ans = [0, 0]
left, right = 0, N - 1
while left < right:
    temp_sum = arr[left] + arr[right]
    if max_diff > abs(temp_sum):
        max_diff = abs(temp_sum)
        ans[0], ans[1] = arr[left], arr[right]
    if temp_sum < 0:
        left += 1
    elif temp_sum > 0:
        right -= 1
    else:
        break
println(f"{ans[0]} {ans[1]}")
