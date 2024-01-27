from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def good(distance, arr):
    global C
    cnt = 1
    before = arr[0]
    for house in arr[1:]:
        if house - before >= distance:
            cnt += 1
            before = house
        if cnt >= C:
            return True
    return False


N, C = map(int, input().split())
arr = []
for n in range(N):
    arr.append(int(input()))
arr.sort()

max_distance = arr[-1] - arr[0]
if C == 2:
    println(max_distance)
    exit()

left, right = 0, max_distance
while left <= right:
    mid = (left + right) // 2
    if good(mid, arr):
        left = mid + 1
    else:
        right = mid - 1
println(right)
