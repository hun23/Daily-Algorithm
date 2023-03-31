N = int(input())
arr = list(map(int ,input().split()))
dp = [list() for _ in range(N)]
dp[N - 1] = [arr[N-1]]

for n in range(N-1 -1, -1, -1):
    # print(dp)
    temp, idx = 0, 0
    for i in range(n + 1, N):
        if arr[n] < arr[i]:
            if temp < len(dp[i]):
                idx = i
                temp = len(dp[i])
    # print(idx)
    temp_list = dp[idx][:]
    # print(temp_list)
    temp_list.append(arr[n])
    dp[n] = list(sorted(temp_list))
# print(dp)
# print(len(dp[0]))
# print(dp)
print(max(map(lambda x: len(x), dp)))
