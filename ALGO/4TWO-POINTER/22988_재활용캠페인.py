from sys import stdin, stdout
from heapq import heapify, heappop, heappush

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def condition(arr, X):
    arr_len = len(arr)
    if arr_len == 0:
        return False
    elif arr_len == 1:
        # 체크 안해도 될듯?
        # temp = heappop(arr)
        # if temp == X:

        return False
    return True


N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 최소횟수 X, 최대개수 O
# 일단 arr에서 X용량은 제외
# C <= X 이므로 정렬하고 cut
ans = 0
arr.sort()
if arr[-1] == X:
    max_idx = arr.index(X)
    ans += N - max_idx
    arr = arr[:max_idx]
# 최소낭비 = A+B가 X/2를 넘어가되 최소로만
# 4 6, 2 3 3 4


left, right = 0, 1
delete_later = []
while left < right:
    temp_sum = arr[left] + arr[right]
    if temp_sum == X:
        ans += 1
        delete_later.append(arr[left])
        delete_later.append(arr[right])
        left += 1
        right -= 1
    elif temp_sum > X:
        right -= 1
    elif temp_sum < X:
        left += 1
for d in delete_later:
    arr.remove(d)
