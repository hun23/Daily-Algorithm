a, b, v = map(int, input().split())
# 매일 올라가는 높이
daily = a - b
# 마지막날 전까지 올라가야 하는 최소 높이
before_last_day = v - a
# 최소높이까지 올라가는데 걸리는 일수
days_minus_one = before_last_day // daily + (
    1 if before_last_day % daily != 0 else 0
)
# 아까 구한 일수 + 마지막날(=1)
print(days_minus_one + 1)
