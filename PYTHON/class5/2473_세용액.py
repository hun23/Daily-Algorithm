def solve():
    global BIG, answer_value, answer, arr, N

    for start in range(N - 2):
        left, right = start + 1, N - 1
        while left < right:
            mid_value = arr[left] + arr[right] + arr[start]
            if abs(mid_value) < answer_value:
                answer = (start, left, right)
                answer_value = abs(mid_value)
                if answer == 0:
                    print(arr[answer[0]], arr[answer[1]], arr[answer[2]])
                    exit(0)
            if mid_value < 0:
                left += 1
            else:
                right -= 1
    return

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer_value = float('inf')
answer = (-1, -1, -1)
solve()
print(arr[answer[0]], arr[answer[1]], arr[answer[2]])
