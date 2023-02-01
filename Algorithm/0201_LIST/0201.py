

# 정렬
# 버블 / 카운팅 / 선택 정렬은 바로 구현할 수 있어야
# 나머지로 퀵/삽입/병합정렬이 있다.

# 버블정렬
"""
for i: N - 1 -> 1
    for j: 0 -> i - 1
        if arr[j] > arr[j + 1] 자리바꿈
"""
n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
