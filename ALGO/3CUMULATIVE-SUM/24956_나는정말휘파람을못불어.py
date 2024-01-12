from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


# EE => dp[2] = 1

# EE e / EE E, dp[i - 1] * 2
# Ee E / eE E, (i - 1) => dp[3] = 4

# EEe e / EEE e / EeE e / eEE e = dp[4 - 1]
# EEe E / EEE E / EeE E / eEE E = dp[4 - 1]
# Eee E / eEe E / eeE E = i - 1
# dp[4] = 4 * 2 + (4 - 1) = 11

# dp[0], dp[1] = 0
# dp[i] = dp[i - 1] * 2 + (i - 1)


def update_dp(e_count):
    global dp, big
    for i in range(2, e_count + 1):
        dp[i] = (dp[i - 1] * 2 + (i - 1)) % big
    return dp[e_count]

big = 1_000_000_007
N = int(input())
whee = input().strip()

w_count = 0
wh_indexes = []
prefix_sum = [0] * N

for i, c in enumerate(whee):
    if c == "E":
        prefix_sum[i] = prefix_sum[i - 1] + 1
        continue

    prefix_sum[i] = prefix_sum[i - 1]
    if c == "W":
        w_count += 1
    elif c == "H":
        wh_indexes.append((i, w_count))

ans = 0
dp = [0] * (200_000 + 1)
update_dp(200_000)

for idx, w_count in wh_indexes:
    e_count = prefix_sum[-1] - prefix_sum[idx]
    ans += dp[e_count] * w_count
    ans %= big

# println(prefix_sum)
# println(wh_indexes)
# println(dp)
println(ans)
