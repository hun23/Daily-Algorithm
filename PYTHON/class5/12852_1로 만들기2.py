N = int(input())
dp = [list()] * (N + 1)
dp[0] = []
dp[1] = [1]
n = 2
while n <= N:
    temp = float('inf')
    case = 0
    if n >= 1:
        if temp >= len(dp[n - 1]) + 1:
            temp = len(dp[n - 1]) + 1
            path = dp[n - 1]
            case = 1
    if n % 2 == 0:
        if temp >= len(dp[n // 2]) + 1:
            temp = len(dp[n // 2]) + 1
            path = dp[n // 2]
            case = 2
    if n % 3 == 0:
        if temp >= len(dp[n // 3]) + 1:
            temp = len(dp[n // 3]) + 1
            path = dp[n // 3]
            case = 3
    new_path = path[:]
    if case == 1:
        new_path.append(path[-1] + 1)
    elif case == 2:
        new_path.append(path[-1] * 2)
    elif case == 3:
        new_path.append(path[-1] * 3)
    dp[n] = new_path
    n += 1
    # print(new_path)
    # print(dp)
print(len(dp[-1]) - 1)
print(*reversed(dp[-1]))
