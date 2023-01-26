n = int(input())
arr = [-1] + list(map(int, input().split()))
student_num = int(input())
student_arr = []
for _ in range(student_num):
    student_arr.append(tuple(map(int, input().split())))
for (s, num) in student_arr:
    if s == 1:
        for multi in range(num, n + 1, num):
            arr[multi] = 1 if arr[multi] == 0 else 0
    else:
        arr[num] = 1 if arr[num] == 0 else 0
        left = num
        right = num
        while True:
            left = left - 1
            right = right + 1
            if 0 < left and right <= n:
                if arr[left] == arr[right]:
                    arr[left] = 1 if arr[left] == 0 else 0
                    arr[right] = 1 if arr[right] == 0 else 0
                else:
                    break
            else:
                break
for (i, status) in enumerate(arr[1:]):
    print(status, end=("\n" if i % 20 == 19 else " "))
