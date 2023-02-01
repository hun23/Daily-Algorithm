T = int(input())
for tc in range(T + 1):
    N = int(input())
    sum_ = 0
    mid = N // 2 + 1
    for i in range(N):
        inp = [int(c) for c in input()]
        if i < mid:
            rem = i % mid
        else:
            rem = N - 1 - i % mid
        for j in range(mid - rem, mid + 1 + rem):
            sum_ += inp[j]

    print(f"#{tc} {sum_}")