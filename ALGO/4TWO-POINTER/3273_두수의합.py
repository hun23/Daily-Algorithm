from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

ans = 0
left, right = 0, N - 1
while left < right:
    temp = arr[left] + arr[right]
    if temp < x:
        left += 1
    elif temp > x:
        right -= 1
    else:
        left += 1
        right -= 1
        ans += 1
println(ans)
