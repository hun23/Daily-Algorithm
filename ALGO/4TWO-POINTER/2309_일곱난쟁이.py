from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


total = 0
arr = []
for i in range(9):
    arr.append(int(input()))
    total += arr[-1]

arr.sort()
target = total - 100
left, right = 0, 8
while left < right:
    temp_sum = arr[left] + arr[right]
    if temp_sum < target:
        left += 1
    elif temp_sum > target:
        right -= 1
    else:
        break
for i in range(9):
    if i == left or i == right:
        continue
    println(arr[i])
