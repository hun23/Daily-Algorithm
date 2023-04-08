# def solve(left, right):
#     global BIG, answer_value, answer, arr
#     if left >= right:
#         return
#     elif left + 1 == right:
#         value = abs(arr[left] + arr[right])
#         if value < answer_value:
#             answer_value = value
#             answer = (left, right)
#         return

#     mid = (left + right) // 2
#     solve(left, mid)  # search left half
#     solve(mid, right)  # search right half
    
#     while left < mid and mid < right:
#         mid_value = arr[left] + arr[right]
#         if abs(mid_value) < answer_value:
#             answer = (left, right)
#             answer_value = abs(mid_value)
#             if answer == 0:
#                 print(arr[answer[0]], arr[answer[1]])
#                 exit(0)
#         if mid_value < 0:
#             left += 1
#         else:
#             right -= 1
#     return

def solve(left, right):
    global BIG, answer_value, answer, arr

    while left < right:
        mid_value = arr[left] + arr[right]
        if abs(mid_value) < answer_value:
            answer = (left, right)
            answer_value = abs(mid_value)
            if answer == 0:
                print(arr[answer[0]], arr[answer[1]])
                exit(0)
        if mid_value < 0:
            left += 1
        else:
            right -= 1
    return

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
BIG = 2000000000
answer_value = BIG
answer = (-1, -1)
solve(0, N - 1)
print(arr[answer[0]], arr[answer[1]])
