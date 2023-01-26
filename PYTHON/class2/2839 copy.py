# DP & greedy


def divide(arr, n):
    if arr[n] != -2:
        return arr[n]
    _min = 2147483647
    if n % 5 == 0:
        _min = n // 5
    elif n % 3 == 0:
        _min = n // 3
    for left in range(1, n):
        right = n - left
        if arr[left] == -2:
            arr[left] = divide(arr, left)
        if arr[right] == -2:
            arr[right] = divide(arr, right)
        if arr[left] == -1 or arr[right] == -1:
            continue
        if _min > arr[left] + arr[right]:
            _min = arr[left] + arr[right]
    if _min == 2147483647:
        _min = -1
    arr[n] = _min
    return _min


n = int(input())
three = 0
five = 0
# 0 ~ n 무게의 횟수 arr를 -2(=아직계산안함)로 초기화
arr = [-2 for _ in range(n + 1)]
try:
    arr[0] = 0  # 0kg짜리는 0회
    arr[1] = -1  # 1kg짜리는 불가능
    arr[2] = -1
    arr[3] = 1  # 3kg짜리는 가능
    arr[4] = -1
    arr[5] = 1  # 5kg짜리도 가능
except:
    pass
# for w in range(n + 1):
#     if arr[w] == -2:
#         arr[w] = divide(arr, n)
print(divide(arr, n))
print(arr)
