T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    idx = 0
    mid = N // 2
    answer = 0
    direction = 1
    # print(arr[mid - idx : mid + 1 + idx])
    for r in range(N):
        answer += sum(arr[r][mid - idx : mid + 1 + idx])
        idx += direction
        if idx > mid:
            direction = -1
            idx = mid - 1
    print(f"#{tc} {answer}")
