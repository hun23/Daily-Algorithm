N, S = map(int, input().split())
arr = list(map(int, input().split()))
cum_sum = [0] * (N + 1)  # cum_sum[0] = 0
for n in range(1, N + 1):  # cum_sum[1] = arr[0]
    cum_sum[n] = cum_sum[n-1] + arr[n - 1]

answer = 0
left, right = 0, 0
while cum_sum[right] < S:
    right += 1
    if right > N:  # if impossible
        print(0)
        exit(0)

answer = (left, right)
while 0 <= left < right <= N:
    temp = cum_sum[right] - cum_sum[left]
    if temp < S:
        right += 1
    else:
        if right - left < answer[1] - answer[0]:
            answer = (left, right)
        left += 1

print(answer[1] - answer[0])
