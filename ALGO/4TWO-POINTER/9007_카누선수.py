from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


T = int(input())
for t in range(T):
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(4)]

    pairs = [[], []]
    for a in range(N):
        for b in range(N):
            pairs[0].append(arr[0][a] + arr[1][b])  # 1반과 2반에서 하나씩 뽑는 경우의 수
    for c in range(N):
        for d in range(N):
            pairs[1].append(arr[2][c] + arr[3][d])  # 3반과 4반

    # 투 포인터 위한 정렬
    pairs[0].sort()
    pairs[1].sort()

    result = [0, 40_000_001]  # K보다 작은 것 중 가장 큰 값, K보다 큰 것 중 가장 작은 값 저장
    left, right = 0, len(pairs[1]) - 1
    while left < len(pairs[0]) and 0 <= right:
        temp_sum = pairs[0][left] + pairs[1][right]
        if temp_sum > K:
            right -= 1
            if temp_sum < result[1]:
                result[1] = temp_sum
        elif temp_sum < K:
            left += 1
            if temp_sum > result[0]:
                result[0] = temp_sum
        else:
            result[0], result[1] = temp_sum, temp_sum
            break
    if result[0] == 0:  # 합이 K보다 작은 경우의 수가 없는 경우
        ans = result[1]
    elif result[1] == 40_000_001:  # 합이 K보다 큰 경우의 수가 없는 경우
        ans = result[0]
    else:  # 그 외의 경우 K와 차이가 더 적은 것
        if K - result[0] > result[1] - K:
            ans = result[1]
        else:
            ans = result[0]
    println(f"{ans}")
