import random

def recur(idx, prev, length, temp):
    global N, arr, dp
    if idx == N + 1:
        return length
    
    if dp[idx][prev] != -1:
        return dp[idx][prev]
    
    ret2 = 0
    if arr[prev] < arr[idx]:
        ret2 = recur(idx + 1, idx, length + 1, temp + [arr[idx]])
    ret1 = recur(idx + 1, prev, length, temp)
    
    if ret1 < ret2:
        dp[idx][prev] = ret2
    else:
        dp[idx][prev] = ret1
    return dp[idx][prev]

def recur2(cur, prev):
    global N, arr, dp
    if cur == N:
        return 0

    if dp[cur][prev] != -1:
        return dp[cur][prev]

    cnt = 0
    if prev == -1 or arr[cur] > arr[prev]:
        cnt = 1 + recur2(cur + 1, cur)

    not_cnt = recur2(cur + 1, prev)

    dp[cur][prev] = max(cnt, not_cnt)
    return dp[cur][prev]

N = int(input())
arr = list(map(int, input().split()))
# arr.insert(0, 0)
dp = [[-1] * (N + 1) for _ in range(N + 1)]
# print(recur(0, 0, 0, []))
print(recur2(0, -1))