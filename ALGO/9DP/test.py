import random

def recur(idx, prev, temp):
    global N, arr, dp
    if idx == N + 1:
        return 0
    
    if dp[idx][prev] != -1:
        return dp[idx][prev]
    
    ret2 = 0
    if arr[prev] < arr[idx]:
        ret2 = 1 + recur(idx + 1, idx, temp + [arr[idx]])
    ret1 = recur(idx + 1, prev, temp)
    
    if ret1 < ret2:
        dp[idx][prev] = ret2
    else:
        dp[idx][prev] = ret1
    return dp[idx][prev]

def recur2(cur, prev):
    global N, arr, dp
    if cur == N:
        return 0

    if dp[prev][cur] != -1:
        return dp[prev][cur]

    cnt = 0
    if prev == -1 or arr[cur] > arr[prev]:
        cnt = 1 + recur2(cur + 1, cur)

    not_cnt = recur2(cur + 1, prev)

    dp[prev][cur] = max(cnt, not_cnt)
    return dp[prev][cur]

for t in range(100):
    N = random.randint(1, 1000)
    arr = [(random.randint(1, 1000)) for _ in range(N)]
    arr.insert(0, 0)
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    a = recur(0, 0, [])
    arr = arr[1:]
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    b = recur2(0, -1)
    if a != b:
        print("+" * 80)
        print(N)
        print(*arr)
        print(a, b)
        